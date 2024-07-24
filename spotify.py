import os
import requests
import json

def get_spotify_token(client_id, client_secret, refresh_token):
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret
    }
    response = requests.post(url, headers=headers, data=data)
    response_data = response.json()
    return response_data['access_token']

def play_podcast(access_token, device_id, podcast_uri):
    url = f"https://api.spotify.com/v1/me/player/play?device_id={device_id}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "uris": [podcast_uri]
    })
    response = requests.put(url, headers=headers, data=data)
    return response.status_code

def lambda_handler(event, context):
    client_id = os.getenv(" ") #PLACE CLIENT ID HERE
    client_secret = os.getenv(" ") #PLACE CLIENT SECRET HERE
    refresh_token = os.getenv(" ") #PLACE TOKEN HERE, FOLLOW TUTORIAL
    device_id = os.getenv(" ") #USE getaccess.py to get THIS!
    podcast_uri = os.getenv("spotify:show:5YRTZNTGT7MWhktYYpjR8v") #EXAMPLE PODCAST, replace with your own following tutorial

    access_token = get_spotify_token(client_id, client_secret, refresh_token)
    status_code = play_podcast(access_token, device_id, podcast_uri)

    return {
        "statusCode": status_code,
        "body": json.dumps("Podcast played successfully.")
    }
