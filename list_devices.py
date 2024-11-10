import os
from wyze_sdk import Client
from wyze_sdk.errors import WyzeApiError

# Set your access token as an environment variable
os.environ['WYZE_ACCESS_TOKEN'] = '[your access token]'

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
