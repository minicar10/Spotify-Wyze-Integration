import os
from wyze_sdk import Client

# Set your Wyze email, password, API key, and key ID as environment variables
os.environ['WYZE_EMAIL'] = 'zachalexjoseph@yahoo.com'
os.environ['WYZE_PASSWORD'] = 'Zach12345!'
os.environ['WYZE_API_KEY'] = 'mYsAmCb1DAboktgSIHpyerk2ZRE9gmySUVo5KPSDWz9AUIvFL8sSYtFo3SO8'
os.environ['WYZE_KEY_ID'] = '03caf13a-7a11-427f-82c2-caeb19a46453'

# Authenticate and get access tokens
response = Client().login(
    email=os.environ['WYZE_EMAIL'],
    password=os.environ['WYZE_PASSWORD'],
    key_id=os.environ['WYZE_KEY_ID'],
    api_key=os.environ['WYZE_API_KEY']
)

print(f"access token: {response['access_token']}")
print(f"refresh token: {response['refresh_token']}")
