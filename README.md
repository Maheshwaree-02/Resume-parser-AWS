# 🚀 Serverless Resume Parser (Mini ATS)

## 📌 Overview
This project is a serverless application that automatically extracts structured information from resumes.

## 🏗️ Architecture
- Amazon S3 → File Upload
- AWS Lambda → Processing
- Amazon Comprehend → NLP
- DynamoDB → Storage
- Streamlit → UI Dashboard

## ⚙️ Workflow
1. Upload resume to S3
2. Lambda is triggered
3. Resume is processed
4. Data stored in DynamoDB
5. Displayed in Streamlit UI

## 🛠️ Tech Stack
- AWS (S3, Lambda, DynamoDB, Comprehend)
- Python (boto3)
- Streamlit

## 🎯 Features
- Automatic resume parsing
- NLP-based key phrase extraction
- Interactive dashboard
- Search functionality

## 📸 Output
(Add screenshots here)

## 👥 Team Contribution
- Infrastructure: AWS setup
- Backend: Lambda + NLP
- Frontend: Streamlit UI
