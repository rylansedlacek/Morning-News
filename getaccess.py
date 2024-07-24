import requests

def get_access_token(client_id, client_secret, refresh_token):
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
    return response.json()['access_token']

def get_devices(access_token):
    url = "https://api.spotify.com/v1/me/player/devices"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    return response.json()

client_id = " " #PUT YOUR ID HERE -- EASY TO FIND
client_secret = " " #PUT YOUR SECRET HERE -- EASY TO FIND
refresh_token = " " #FOLLOW THE TUTORIAL BELOW TO GET YOUR TOKEN

access_token = get_access_token(client_id, client_secret, refresh_token)
devices = get_devices(access_token)

print(devices)
