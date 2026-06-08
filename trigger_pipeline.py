import requests
import base64
import time
import json
import sys




def trigger_pipeline():
    client_id = "dataopssuite-restapi-client"
    client_secret = "!e#lRR7Q"
    username = "Anitha"
    password = "U2FsdGVkX19boJtjLVCVq6OIe85wofMZZy6poJ8KvzI0gwlA6YqjU9Dm235ELVOY"
    pipeline_id = "6fab0a0e-f2f3-4ea8-b194-0b67ec08bc83"

    auth_url = "https://dgvm6205.datagapsinc.in/dataopssecurity/oauth2/token"
    basic_auth_str = f"{client_id}:{client_secret}"
    base64_auth_str = base64.b64encode(basic_auth_str.encode()).decode()

    headers = {
        "Authorization": f"Basic {base64_auth_str}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {
        "username": username,
        "password": password,
        "grant_type": "password"
    }

    response = requests.post(auth_url, headers=headers, data=payload)
    if response.status_code != 200:
        print(f"Auth failed: {response.status_code}, {response.text}")
        sys.exit(1)

    access_token = response.json().get("access_token")
    print(access_token)
    print(" Authentication successful")


trigger_pipeline()





