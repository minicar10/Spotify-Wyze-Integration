import os
import requests
import hashlib

# Replace these values with your email and password
WYZE_EMAIL = '[your email address]'
WYZE_PASSWORD = '[your password]'

# Login endpoint details
login_url = "https://auth-prod.api.wyze.com/api/user/login"

# Function to hash the password three times using MD5
def hash_password(password):
    for _ in range(3):
        password = hashlib.md5(password.encode()).hexdigest()
    return password

# Payload for the login request
payload = {
    "email": WYZE_EMAIL,
    "password": hash_password(WYZE_PASSWORD)
}

# Headers for the request
headers = {
    "Content-Type": "application/json"
}

# Make the POST request to login and get tokens
response = requests.post(login_url, json=payload, headers=headers)

if response.status_code == 200:
    response_data = response.json()
    print("Response JSON:", response_data)
    access_token = response_data.get('access_token')
    refresh_token = response_data.get('refresh_token')
    print(f"Access token: {access_token}")
    print(f"Refresh token: {refresh_token}")
else:
    print(f"Failed to get tokens: {response.status_code}")
    print("Response JSON:", response.json())
