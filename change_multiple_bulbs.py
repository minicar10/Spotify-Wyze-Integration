import os
import requests
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from PIL import Image, ImageGrab
import numpy as np
from sklearn.cluster import KMeans
import time
import pygetwindow as gw
import pyautogui

# Spotify API credentials
SPOTIPY_CLIENT_ID = '[your client id here]'
SPOTIPY_CLIENT_SECRET = '[your client secret here]'
SPOTIPY_REDIRECT_URI = '[your redirect uri here]'

# Wyze access token
WYZE_ACCESS_TOKEN = '[your access token here]'

# Spotify authorization
scope = "user-read-playback-state"

sp = Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                       client_secret=SPOTIPY_CLIENT_SECRET,
                                       redirect_uri=SPOTIPY_REDIRECT_URI,
                                       scope=scope))

# Function to get the dominant color using K-means clustering
def get_dominant_color(image, k=4, image_processing_size=(100, 100)):
    # Resize image to reduce computation
    image = image.resize(image_processing_size)
    image = np.array(image)
    
    # Reshape image to be a list of pixels
    pixels = image.reshape((-1, 3))
    
    # Remove white colors and very bright colors
    pixels = np.array([pixel for pixel in pixels if np.all(pixel < 250)])
    
    # Perform K-means clustering
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(pixels)
    colors = kmeans.cluster_centers_

    # Get the most frequent color
    labels = kmeans.labels_
    label_counts = np.bincount(labels)

    # Find the most frequent color index
    dominant_color_index = np.argmax(label_counts)
    dominant_color = colors[dominant_color_index]
    
    return tuple(int(c) for c in dominant_color)

# Function to set bulb color
def set_bulb_color(color):
    from wyze_sdk import Client
    from wyze_sdk.errors import WyzeApiError

    client = Client(token=WYZE_ACCESS_TOKEN)
    bulbs = [
        {'mac': '7C78B23FF2FC', 'model': 'WLPA19C'},  # Color Bulb 2
        {'mac': '7C78B2591F23', 'model': 'WLPA19C'},  # Color Bulb 1
    ]
    hex_color = f'{color[0]:02x}{color[1]:02x}{color[2]:02x}'

    try:
        for bulb in bulbs:
            client.bulbs.set_color(device_mac=bulb['mac'], device_model=bulb['model'], color=hex_color)
            bulb_info = client.bulbs.info(device_mac=bulb['mac'])
            print(f"Changed color of bulb {bulb['mac']} to: {bulb_info.color}")
    except WyzeApiError as e:
        print(f"Got an error: {e}")

# Monitor the current playing track
current_track_id = None
while True:
    current_playback = sp.current_playback()
    if current_playback and current_playback['is_playing']:
        track = current_playback['item']
        track_id = track['id']
        if track_id != current_track_id:
            current_track_id = track_id
            
            # Find the Spotify window
            windows = gw.getWindowsWithTitle('Spotify')
            if windows:
                spotify_window = windows[0]

                # Take a screenshot of the Spotify window without activating it
                left = spotify_window.left
                top = spotify_window.top
                width = spotify_window.width
                height = spotify_window.height
                
                screenshot = pyautogui.screenshot(region=(left, top, width, height))
                
                # Get the dominant color from the screenshot
                dominant_color = get_dominant_color(screenshot)
                
                # Set the bulb color to the dominant color
                set_bulb_color(dominant_color)
    time.sleep(5)  # Wait for 5 seconds before checking again
