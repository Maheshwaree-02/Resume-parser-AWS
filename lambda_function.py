import boto3
import uuid
import urllib.parse
import re
import json
from datetime import datetime

# Initialize AWS clients
s3 = boto3.client('s3')
comprehend = boto3.client('comprehend', region_name='us-east-1')
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('ResumeParsedData')

def lambda_handler(event, context):
    print("Event:", json.dumps(event))

    for record in event.get('Records', []):
        bucket = record['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(record['s3']['object']['key'])

        print(f"Processing file: {key}")

        try:
            # 🔹 1. FETCH FILE FROM S3
            response = s3.get_object(Bucket=bucket, Key=key)
            text = response['Body'].read().decode('utf-8')

            if not text.strip():
                print("Empty file, skipping...")
                continue

            print("File read successfully")

            # 🔹 2. TRANSFORM (Extract structured data)

            # Extract Email
            email_match = re.search(r'[\w\.-]+@[\w\.-]+', text)
            email = email_match.group(0) if email_match else "Not Found"

            # Clean lines
            lines = [line.strip() for line in text.split('\n') if line.strip()]

            # Extract Name
            name = lines[0] if lines else "Unknown"

            # Extract Skills
            skills = []
            for line in lines:
                if "skills" in line.lower() and ":" in line:
                    skills = [s.strip() for s in line.split(':', 1)[1].split(',')]
                    break

            print("Extracted:", name, email, skills)

            # 🔹 3. ENRICH (Comprehend NLP)
            key_phrases = []
            try:
                comp_res = comprehend.detect_key_phrases(
                    Text=text[:4900],  # limit safe
                    LanguageCode='en'
                )
                key_phrases = [kp['Text'] for kp in comp_res.get('KeyPhrases', [])]
                print("Key phrases extracted")

            except Exception as e:
                print(f"Comprehend Error: {str(e)}")

            # 🔹 4. LOAD INTO DYNAMODB
            item = {
                'document_id': str(uuid.uuid4()),
                'name': name,
                'email': email,
                'skills': skills,
                'key_phrases': key_phrases,
                'file_name': key,
                'uploaded_at': datetime.utcnow().isoformat()
            }

            table.put_item(Item=item)
            print("Saved to DynamoDB")

        except Exception as e:
            print(f"Error processing {key}: {str(e)}")
            continue

    return {
        'statusCode': 200,
        'body': json.dumps('Processing Complete')
    }