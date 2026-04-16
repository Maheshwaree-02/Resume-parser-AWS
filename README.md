# 🚀 Serverless Resume Parser (Mini ATS)

## 📌 Overview

The **Serverless Resume Parser** is a cloud-based application that automates the extraction of structured information from resumes. It leverages AWS serverless architecture to process uploaded documents and transform unstructured text into meaningful insights such as candidate name, email, skills, and key phrases.

This project simulates the backend of an **Applicant Tracking System (ATS)** and demonstrates real-world cloud integration.

---

## 🏗️ Architecture

```
User (Streamlit UI)
        ↓
Amazon S3 (Resume Upload)
        ↓ (Event Trigger)
AWS Lambda (Processing)
        ↓
Amazon Comprehend (NLP)
        ↓
Amazon DynamoDB (Storage)
        ↓
Streamlit Dashboard (Visualization)
```

---

## ⚙️ Workflow

1. User uploads a resume via Streamlit UI
2. File is stored in Amazon S3
3. S3 triggers AWS Lambda automatically
4. Lambda:

   * Reads the file
   * Extracts name, email, and skills using regex
   * Uses NLP to extract key phrases
5. Processed data is stored in DynamoDB
6. Streamlit dashboard fetches and displays structured data

---

## ☁️ AWS Services Used

* **Amazon S3** – Stores uploaded resumes
* **AWS Lambda** – Serverless compute for processing
* **Amazon Comprehend** – NLP-based key phrase extraction
* **Amazon DynamoDB** – NoSQL database for storing parsed data
* **Amazon CloudWatch** – Logging and monitoring

---

## 🛠️ Tech Stack

* **Cloud**: AWS (S3, Lambda, DynamoDB, Comprehend)
* **Backend**: Python (boto3, regex)
* **Frontend**: Streamlit
* **Version Control**: Git & GitHub

---

## ✨ Features

* 📄 Automated resume parsing
* 🧠 NLP-based key phrase extraction
* ⚡ Event-driven serverless architecture
* 📊 Interactive dashboard UI
* 🔍 Search and filter functionality
* ☁️ Fully scalable and cost-efficient

---


## 📂 Project Structure

```
resume-parser-aws/
│
├── app.py                  # Streamlit Dashboard
├── lambda_function.py      # AWS Lambda Backend Logic
├── README.md
├── .gitignore
```

---

## 🔐 Security & IAM

* IAM Roles used for Lambda to securely access AWS services
* IAM User with access keys used for local Streamlit integration
* No credentials are hardcoded in the codebase

---

## ⚠️ Challenges Faced

* Handling S3 object key encoding (`+` vs spaces)
* Lambda timeout issues during processing
* Amazon Comprehend region availability
* Ensuring proper IAM permissions

---

## 🚀 Future Enhancements

* Support for PDF parsing using Textract
* Advanced skill extraction using ML models
* Resume ranking system
* Deploy Streamlit UI on cloud (EC2 / AWS App Runner)

---

## 🎯 Learning Outcomes

* Hands-on experience with serverless architecture
* Integration of multiple AWS services
* Event-driven system design
* Real-world cloud application development

---

## ⭐ Conclusion

This project demonstrates how modern cloud technologies can be used to build scalable, automated systems with minimal infrastructure management, closely resembling real-world industry applications.

---


