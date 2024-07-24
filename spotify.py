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
    client_id = os.getenv("e15dac3733004dea97472dcb07ca942a")
    client_secret = os.getenv("c3908f746ee44581b04a75f5cf47db35")
    refresh_token = os.getenv("AQCCtUmwzoDhi5xGXWKqWzCTw9LyCQsVhQs-8CEGZadRmM5F7HR8ZV-luGwmefKPkjIo7pU16dxVwIwlmFRusCtZ42B4Sbl5Ly8SnQ64HR_7UB2xtcT1CAp6PJzCYZ3MvyQ")
    device_id = os.getenv("7e35837d51098501682dfaf24f189c03f0c1dda6")
    podcast_uri = os.getenv("spotify:show:5YRTZNTGT7MWhktYYpjR8v")

    access_token = get_spotify_token(client_id, client_secret, refresh_token)
    status_code = play_podcast(access_token, device_id, podcast_uri)

    return {
        "statusCode": status_code,
        "body": json.dumps("Podcast played successfully.")
    }
