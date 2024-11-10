import time
from wyze_sdk import Client
from wyze_sdk.errors import WyzeApiError

# Wyze access token
WYZE_ACCESS_TOKEN = '[your access token here]'

# Wyze bulbs
bulbs = [
    {'mac': '[your mac address]', 'model': '[your model]'},  # Color Bulb 2
    {'mac': '[your mac address]', 'model': '[your model]'},  # Color Bulb 1
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
