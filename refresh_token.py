import os
import requests

# Replace this value with your actual refresh token
WYZE_REFRESH_TOKEN = '[your refresh token]'

# Refresh token endpoint details
refresh_token_url = "https://api.wyzecam.com/app/user/refresh_token"

# Payload for the refresh token request
payload = {
    "app_ver": "wyze_developer_api",
    "app_version": "wyze_developer_api",
    "phone_id": "wyze_developer_api",
    "refresh_token": WYZE_REFRESH_TOKEN,
    "sc": "wyze_developer_api",
    "sv": "wyze_developer_api",
    "ts": 4070908800000
}

# Headers for the request
headers = {
    "Content-Type": "application/json"
}

# Make the POST request to refresh the token
response = requests.post(refresh_token_url, json=payload, headers=headers)

if response.status_code == 200:
    response_data = response.json()
    print("Response JSON:", response_data)
    data = response_data.get('data', {})
    new_access_token = data.get('access_token')
    new_refresh_token = data.get('refresh_token')

    # Save the new tokens to a file
    with open('tokens.txt', 'w') as f:
        f.write(f"ACCESS_TOKEN={new_access_token}\n")
        f.write(f"REFRESH_TOKEN={new_refresh_token}\n")
    
    print(f"New access token: {new_access_token}")
    print(f"New refresh token: {new_refresh_token}")
else:
    print(f"Failed to refresh token: {response.status_code}")
    print("Response JSON:", response.json())
