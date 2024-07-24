import requests
import os

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
    
    if 'access_token' in response_data:
        return response_data['access_token']
    else:
        error_message = response_data.get('error', 'No error message provided')
        error_description = response_data.get('error_description', 'No error description provided')
        raise Exception(f"Error getting access token: {error_message} - {error_description}")

def play_podcast(access_token, podcast_uri):
    url = "https://api.spotify.com/v1/me/player/play"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "context_uri": podcast_uri
    }
    response = requests.put(url, headers=headers, json=data)
    
    
    if response.status_code != 200:
        raise Exception(f"Failed to play podcast: {response.status_code} - {response.text}")

def lambda_handler(event, context):
    client_id = os.environ['SPOTIFY_CLIENT_ID']
    client_secret = os.environ['SPOTIFY_CLIENT_SECRET']
    refresh_token = os.environ['SPOTIFY_REFRESH_TOKEN']
    podcast_uri = os.environ['SPOTIFY_PODCAST_URI']  

    try:
        access_token = get_spotify_token(client_id, client_secret, refresh_token)
        play_podcast(access_token, podcast_uri)
        
        return {
            'statusCode': 200
            'body': 'Podcast playback initiated successfully.'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
