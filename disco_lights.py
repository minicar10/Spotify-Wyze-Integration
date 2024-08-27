import time
from wyze_sdk import Client
from wyze_sdk.errors import WyzeApiError

# Wyze access token
WYZE_ACCESS_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhiN2Y4YmMwLWFhNWQtNDJmNi04MmY2LWZlZjFlMzFjN2M4NyJ9.eyJhdWQiOlsib2F1dGgyLXJlc291cmNlIiwibmF0aXZlX29hdXRoMl9yZXNvdXJjZSJdLCJ1c2VyX2lkIjoiZDkzZWExNTk1MWYzNzMyMzY1YjVlNDgzMTVlZDBlYmQiLCJ1c2VyX25hbWUiOiJ6YWNoYWxleGpvc2VwaEB5YWhvby5jb20iLCJzY29wZSI6WyJuYXRpdmUiXSwiaXNzIjoiaHR0cHM6Ly9hdXRoLnd5emUuY29tIiwiY3JlYXRlZF9hdCI6MTcyMTUzMTY4MCwiZXhwIjoxNzIxNTM3NjgwLCJhdXRob3JpdGllcyI6WyJVU0VSIl0sImp0aSI6IlhyeXdTYkhiN3Y2N2dRZkNHUkNFcUlxMnpRayIsImNsaWVudF9pZCI6IjhjMGUwM2NhLTA3NjAtNDI5ZS1hNTdiLTkxYzNkZGEwZjFiOCJ9.FoLz3vvK955FjjlFSv-3YFgUpxZmX2bTAo_v8_5jpZ1kanhfJJWyw8b1-jXnBMzpdbJ3mfYJ3EX7XSu-kzDzOvQE_8grvulo_tzQWgXD8KirKHbZY6mVO8sVeSJuVIoDATUBMOSdO5Vt0cVy-EM3-Yzg5oEYLhFghT9swrBdQZ6wbFgppRQoc0lRHbeG0kl4obJ_caMlNOPUrQuAwa7adOoXFVFjXEVpZsgN9UeP7U-pYbQz3Y8MnSslg8hl0N-0XjmHPGx1QsUIz7nII798jArg9QAxnWWZTpZx1hdXG1c_Fo8gI-HXDZMx2z95VIV3L_YugQnvSJ7FTB_xSyyvHA'

# Wyze bulbs
bulbs = [
    {'mac': '7C78B23FF2FC', 'model': 'WLPA19C'},  # Color Bulb 2
    {'mac': '7C78B2591F23', 'model': 'WLPA19C'},  # Color Bulb 1
]

def set_color(client, bulb, color):
    try:
        client.bulbs.set_color(device_mac=bulb['mac'], device_model=bulb['model'], color=color)
    except WyzeApiError as e:
        print(f"Error setting color for bulb {bulb['mac']}: {e}")

def disco_lights(client, bulbs):
    colors = ['ff0000', '00ff00', '0000ff']  # Red, Green, Blue
    while True:
        for color in colors:
            for bulb in bulbs:
                set_color(client, bulb, color)
            time.sleep(1)  # Wait for 1 second before changing color

if __name__ == "__main__":
    client = Client(token=WYZE_ACCESS_TOKEN)
    disco_lights(client, bulbs)
