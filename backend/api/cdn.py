import requests
import json
from django.core.files.uploadedfile import InMemoryUploadedFile
from dotenv import load_dotenv
import os


load_dotenv()

# First, get a token

TOKEN_URL = os.getenv("TOKEN_URL") #'https://api.sirv.com/v2/token'
UPLOAD_URL = os.getenv("UPLOAD_URL")#'https://api.sirv.com/v2/files/upload'
STAT_URL = os.getenv("STAT_URL")#'https://api.sirv.com/v2/files/stat'
CDN_URL = os.getenv("CDN_URL")#'https://image-encrypter.sirv.com'
CLIENT_ID = os.getenv("CLIENT_ID") #'FKvkcjfNP2cipKi7Bp8fk7tkEiV'
CLIENT_SECRET = os.getenv("CLIENT_SECRET") #'td+IqHPUUptndGwvneT0drcQ0DpeIBEOd2roxgmwPG6NdQfRtXd4g2VGJXogMwfOLnxgYxFWxz+LdFH9trG4GA=='


def get_token():
    payload = {
        'clientId': CLIENT_ID,
        'clientSecret': CLIENT_SECRET
    }

    headers = {'content-type': 'application/json'}

    response = requests.request('POST', TOKEN_URL, data=json.dumps(payload), headers=headers)
    token = response.json()['token']
    return token

def file_already_exists(file_name: str, username: str, bearer_token: str):
    headers = {
        'content-type': 'application/json',
        'authorization': 'Bearer %s' % bearer_token
    }
    
    querystring = {'filename': f'/uploaded_images/{username}/{file_name}'}  
    response = json.loads(requests.get(STAT_URL, headers=headers, params=querystring).text)
    return "statusCode" not in response and not response["isDirectory"]
    


# upload file

def upload_file(file: InMemoryUploadedFile, username: str, file_name: str, override: bool):
    bearer_token = get_token()
    if not override and file_already_exists(file_name, username, bearer_token):
        return {
            'status': '409',
            'text': f'File {file_name} already exists',
        }
    
    querystring = {'filename': f'/uploaded_images/{username}/{file_name}'}  
    
    headers = {
        'content-type': file.content_type,
        'authorization': 'Bearer %s' % bearer_token
    }

    response = requests.post(UPLOAD_URL, data=file, headers=headers, params=querystring)

    output = {
        'status': response.status_code,
        'text': response.text,
        'url': f'{CDN_URL}/uploaded_images/{username}/{file_name}'
    }

    return output
 
 
 