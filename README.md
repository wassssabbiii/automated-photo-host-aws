# Automated Photo Web-Host with AWS IAM Access Keys

## Project Overview
This project demonstrates **programmatic cloud integration** by using a local Python script to interact securely with Amazon S3. 

The application utilizes a dedicated IAM service user with strictly scoped programmatic access keys to automatically upload localized media (`test.jpg`) to an S3 bucket configured for public static website hosting. 

---

## Architecture & Security Workflow



1. **Least Privilege Control:** The script's IAM identity is locked down via a custom JSON policy allowing *only* `s3:PutObject` actions. It cannot read, delete, or modify any other structural cloud components.
2. **Bucket-Level Isolation:** The S3 bucket permissions explicitly decouple administrative write rights from public read access. The public can view the website objects via an anonymous `s3:GetObject` bucket policy, but only our credentialed script can populate it.
3. **Environment Security:** Operational AWS Access Keys are abstracted completely out of source control using `.env` files and `.gitignore` patterns to eliminate credential leakage risks.

---

## Technologies Used
* **Python 3**
* **Boto3** (AWS SDK for Python)
* **Amazon S3** (Object Storage & Static Website Hosting)
* **AWS IAM** (Programmatic Access Keys & Custom Policies)
* **Dotenv** (Environment Variable Management)
