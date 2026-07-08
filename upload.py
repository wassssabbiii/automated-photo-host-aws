import os
import boto3
from dotenv import load_dotenv

# Load credentials from .env file
load_dotenv()

# Initialize S3 client using environment variables
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

bucket_name = os.getenv('AWS_BUCKET_NAME')

def upload_photo(file_path, object_name):
    try:
        print(f"Uploading {file_path} to S3...")
        s3.upload_file(file_path, bucket_name, object_name)
        print("Upload successful!")
        
        # Print out the public web link to your photo
        print(f"View your photo here: http://{bucket_name}.s3.amazonaws.com/{object_name}")
    except Exception as e:
        print(f"Error occurred: {e}")

# Test the upload (Make sure you have a sample image named 'test.jpg' in your folder!)
upload_photo('test.jpg', 'my-portfolio-pic.jpg')