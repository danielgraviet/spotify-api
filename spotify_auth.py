import requests
import base64

# Replace these with your actual credentials
CLIENT_ID = '755199180be3403995ce1eb9c5f082b4'
CLIENT_SECRET = '5b541de87b51401689d497d60f91e2be'

def get_access_token():
    # Create a base64 encoded string of client ID and client secret
    client_creds = f"{CLIENT_ID}:{CLIENT_SECRET}"
    client_creds_b64 = base64.b64encode(client_creds.encode()).decode()

    # Set the request headers and data
    headers = {
        'Authorization': f'Basic {client_creds_b64}',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'grant_type': 'client_credentials'
    }

    # Send a POST request to the token endpoint
    response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)

    if response.status_code == 200:
        token_info = response.json()
        return token_info['access_token']
    else:
        print(f"Error getting access token: {response.status_code} - {response.text}")
        return None