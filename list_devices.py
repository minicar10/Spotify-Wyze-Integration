import os
from wyze_sdk import Client
from wyze_sdk.errors import WyzeApiError

# Set your access token as an environment variable
os.environ['WYZE_ACCESS_TOKEN'] = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhiN2Y4YmMwLWFhNWQtNDJmNi04MmY2LWZlZjFlMzFjN2M4NyJ9.eyJhdWQiOlsib2F1dGgyLXJlc291cmNlIiwibmF0aXZlX29hdXRoMl9yZXNvdXJjZSJdLCJ1c2VyX2lkIjoiZDkzZWExNTk1MWYzNzMyMzY1YjVlNDgzMTVlZDBlYmQiLCJ1c2VyX25hbWUiOiJ6YWNoYWxleGpvc2VwaEB5YWhvby5jb20iLCJzY29wZSI6WyJuYXRpdmUiXSwiaXNzIjoiaHR0cHM6Ly9hdXRoLnd5emUuY29tIiwiY3JlYXRlZF9hdCI6MTcyMTUzMTY4MCwiZXhwIjoxNzIxNTM3NjgwLCJhdXRob3JpdGllcyI6WyJVU0VSIl0sImp0aSI6IlhyeXdTYkhiN3Y2N2dRZkNHUkNFcUlxMnpRayIsImNsaWVudF9pZCI6IjhjMGUwM2NhLTA3NjAtNDI5ZS1hNTdiLTkxYzNkZGEwZjFiOCJ9.FoLz3vvK955FjjlFSv-3YFgUpxZmX2bTAo_v8_5jpZ1kanhfJJWyw8b1-jXnBMzpdbJ3mfYJ3EX7XSu-kzDzOvQE_8grvulo_tzQWgXD8KirKHbZY6mVO8sVeSJuVIoDATUBMOSdO5Vt0cVy-EM3-Yzg5oEYLhFghT9swrBdQZ6wbFgppRQoc0lRHbeG0kl4obJ_caMlNOPUrQuAwa7adOoXFVFjXEVpZsgN9UeP7U-pYbQz3Y8MnSslg8hl0N-0XjmHPGx1QsUIz7nII798jArg9QAxnWWZTpZx1hdXG1c_Fo8gI-HXDZMx2z95VIV3L_YugQnvSJ7FTB_xSyyvHA'

client = Client(token=os.environ['WYZE_ACCESS_TOKEN'])

try:
    response = client.devices_list()
    for device in response:
        print(f"mac: {device.mac}")
        print(f"nickname: {device.nickname}")
        print(f"is_online: {device.is_online}")
        print(f"product model: {device.product.model}")
except WyzeApiError as e:
    print(f"Got an error: {e}")