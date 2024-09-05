import requests
import json
from django.core.files.uploadedfile import InMemoryUploadedFile

BEARER_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJZCI6IkZLdmtjamZOUDJjaXBLaTdCcDhmazd0a0VpViIsImNsaWVudE5hbWUiOiJpbWFnZS1lbmNyeXB0ZXIiLCJzY29wZSI6WyJhY2NvdW50OnJlYWQiLCJhY2NvdW50OndyaXRlIiwidXNlcjpyZWFkIiwidXNlcjp3cml0ZSIsImJpbGxpbmc6cmVhZCIsImJpbGxpbmc6d3JpdGUiLCJmaWxlczpyZWFkIiwiZmlsZXM6d3JpdGUiLCJmaWxlczpjcmVhdGUiLCJmaWxlczp1cGxvYWQ6bXVsdGlwYXJ0IiwiZmlsZXM6c2hhcmVkQmlsbGluZyIsInZpZGVvcyIsImltYWdlcyJdLCJpYXQiOjE3MjU0MzAyMDIsImV4cCI6MTcyNTQzMTQwMiwiYXVkIjoiYzNrM2VoancxdGhpdm5za3ptaWhwMzE1dG95bHQ1enQifQ.rcDt9PqgFufEnW8df2srH9gSew3V0hEpRTgeFFMCVpI'

# First, get a token

TOKEN_URL = 'https://api.sirv.com/v2/token'
UPLOAD_URL = 'https://api.sirv.com/v2/files/upload'
CDN_URL = 'https://image-encrypter.sirv.com'
CLIENT_ID = 'FKvkcjfNP2cipKi7Bp8fk7tkEiV'
CLIENT_SECRET = 'td+IqHPUUptndGwvneT0drcQ0DpeIBEOd2roxgmwPG6NdQfRtXd4g2VGJXogMwfOLnxgYxFWxz+LdFH9trG4GA=='

def get_token():
    payload = {
        'clientId': CLIENT_ID,
        'clientSecret': CLIENT_SECRET
    }

    headers = {'content-type': 'application/json'}

    response = requests.request('POST', TOKEN_URL, data=json.dumps(payload), headers=headers)
    token = response.json()['token']
    return token


# upload file

def upload_file(file: InMemoryUploadedFile, host_path: str):
    bearer_token = get_token()
    querystring = {'filename': f'/{host_path}'} 
    headers = {
        'content-type': 'image/png',
        'authorization': 'Bearer %s' % bearer_token
    }

    response = requests.post(UPLOAD_URL, data=file, headers=headers, params=querystring)

    output = {
        'status': response.status_code,
        'text': response.text,
        'url': f'{CDN_URL}/{host_path}'
    }

    return output
 
 
 