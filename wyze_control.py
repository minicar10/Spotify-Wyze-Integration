import os
from wyze_sdk import Client

# Set your Wyze email, password, API key, and key ID as environment variables
os.environ['WYZE_EMAIL'] = '[your email address]'
os.environ['WYZE_PASSWORD'] = '[your password]'
os.environ['WYZE_API_KEY'] = '[your api key]'
os.environ['WYZE_KEY_ID'] = '[your key id]'

# Authenticate and get access tokens
response = Client().login(
    email=os.environ['WYZE_EMAIL'],
    password=os.environ['WYZE_PASSWORD'],
    key_id=os.environ['WYZE_KEY_ID'],
    api_key=os.environ['WYZE_API_KEY']
)

print(f"access token: {response['access_token']}")
print(f"refresh token: {response['refresh_token']}")
