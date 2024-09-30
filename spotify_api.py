import requests
from spotify_auth import get_access_token

def search_track(query, token):
    url = "https://api.spotify.com/v1/search"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    params = {
        'q': query,
        'type': 'track',
        'limit': 1
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        results = response.json()
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            return {
                # 'name': track['name'],
                'artist': track['artists'][0]['name'],
                'total_tracks': track['album']['total_tracks'],
                'release_date': track['album']['release_date'],
                'popularity' : track['popularity'],
                'url': track['album']['images'][0]['url']  # This gets the first image's URL
                # 'album': track['album']['name']
            }
        else:
            return "No results found."
    else:
        return f"Error searching track: {response.status_code} - {response.text}"

if __name__ == "__main__":
    token = get_access_token()
    if token:
        track_info = search_track("SOURDOUGHSTARTER", token)
        print(track_info)
