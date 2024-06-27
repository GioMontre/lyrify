import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json


load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")


scope = "user-read-playback-state user-read-currently-playing"

sp_oauth = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope,
)

sp = spotipy.Spotify(auth_manager=sp_oauth)


def get_currently_playing():
    results = sp.current_playback()
    if results:
        return {
            "Track": results["item"]["name"],
            "Artist": results["item"]["artists"][0]["name"],
        }
    else:
        return {"Track": None, "Artist": None}


def main():
    print(get_currently_playing())


if __name__ == "__main__":
    main()
