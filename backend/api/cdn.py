from django.core.files.uploadedfile import InMemoryUploadedFile
from dotenv import load_dotenv
import os
import boto3
import tempfile
from botocore.exceptions import ClientError

load_dotenv()
BUCKET_NAME = os.getenv("BUCKET_NAME")
s3_upload_client = boto3.client('s3') # use for upload

def file_already_exists(file_name: str, username: str):
    s3_file_path = f'{username}/{file_name}'
    try: 
        s3_upload_client.head_object(Bucket=BUCKET_NAME, Key=s3_file_path)
        return True
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            return False
        else:
            raise e 


def upload_file(file: InMemoryUploadedFile, username: str, file_name: str, override: bool):
    if not override and file_already_exists(file_name, username):
        return {
            'status': '409',
            'text': f'File {file_name} already exists',
        }

    temp_file = tempfile.NamedTemporaryFile(delete=True)
    temp_file.write(file.read())
    temp_file_path = temp_file.name
    
    # Define the file and bucket
    s3_file_path = f'{username}/{file_name}' # File name in S3

    # Upload the file
    s3_upload_client.upload_file(temp_file_path, BUCKET_NAME, s3_file_path)
    temp_file.close() 
    
    if file_already_exists(file_name, username):
        return {
            'status': '200',
            'text': 'File uploaded successfully.',
            'url': f'{username}/{file_name}'
        }
    else:
        return {
            'status': '400',
            'text': 'Server-side error.',
            'url': None
        }
    
 
 