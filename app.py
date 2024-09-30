from spotify_auth import get_access_token
from spotify_api import search_track

def main():
    token = get_access_token()
    if token:
        track_info = search_track("Money Trees", token)
        print(track_info)

if __name__ == "__main__":
    main()
