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

client_id = "e15dac3733004dea97472dcb07ca942a"
client_secret = "c3908f746ee44581b04a75f5cf47db35"
refresh_token = "AQCCtUmwzoDhi5xGXWKqWzCTw9LyCQsVhQs-8CEGZadRmM5F7HR8ZV-luGwmefKPkjIo7pU16dxVwIwlmFRusCtZ42B4Sbl5Ly8SnQ64HR_7UB2xtcT1CAp6PJzCYZ3MvyQ"

access_token = get_access_token(client_id, client_secret, refresh_token)
devices = get_devices(access_token)

print(devices)
