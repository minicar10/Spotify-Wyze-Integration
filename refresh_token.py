import os
import requests

# Replace this value with your actual refresh token
WYZE_REFRESH_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhiN2Y4YmMwLWFhNWQtNDJmNi04MmY2LWZlZjFlMzFjN2M4NyJ9.eyJhdWQiOlsib2F1dGgyLXJlc291cmNlIiwibmF0aXZlX29hdXRoMl9yZXNvdXJjZSJdLCJ1c2VyX2lkIjoiZDkzZWExNTk1MWYzNzMyMzY1YjVlNDgzMTVlZDBlYmQiLCJ1c2VyX25hbWUiOiJ6YWNoYWxleGpvc2VwaEB5YWhvby5jb20iLCJzY29wZSI6WyJuYXRpdmUiXSwiYXRpIjoiZk1MM2ExVVJxZC04NVY0bXJnNERPTDFnMFFnIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLnd5emUuY29tIiwiY3JlYXRlZF9hdCI6MTcyMjIxNDcxOCwiZXhwIjoxNzI0NjMzOTE4LCJhdXRob3JpdGllcyI6WyJVU0VSIl0sImp0aSI6ImYtZVV0dDF4VFV4T0ttOXlCZXN0Rm9zNEJMSSIsImNsaWVudF9pZCI6IjhjMGUwM2NhLTA3NjAtNDI5ZS1hNTdiLTkxYzNkZGEwZjFiOCJ9.XCT46YTDkv7EclAuPrMYy1xt0mvVgwvJjSuPQlyRcuxXJFky13jg6-MM9pRXo8N1XTP4HeT1stwejiVtLI_MuDk_ITWhUVePOaBO4v2hAFIbXNWe8jl0rO9EJvzQJv4gxQxkEKLqXyQ2mDieInjZpYgl3CJ6inoOntGoO7kphevz1B9B7WrVKapZ4rntr-JbrCHoqvYsYoe-org_Fx6gT3NJysegmHyzEbuc3QexYQRF7bd-iYUNmLtn9XyNhJhpOdT01PJ4U-wME_gUsMKXi2NKrsgGEB19EZ9iRezTetY0cxCASyi2P5VlI50sMjNaSzq-M5LXVc038Ocwhezjlw'

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
