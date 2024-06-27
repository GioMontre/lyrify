import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import lyricsgenius as lg
import re


def get_currently_playing():
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

    results = sp.current_playback()
    if results:
        return results["item"]["name"], results["item"]["artists"][0]["name"]


def get_lyrics(song_name, artist):

    load_dotenv()
    genius_id = os.getenv("GENIUS_ID")
    genius = lg.Genius(
        genius_id,
        skip_non_songs=True,
        excluded_terms=["(Remix)", "(Live)"],
    )

    song = genius.search_song(song_name, artist)
    if song:
        print(song.lyrics)
    else:
        print("Lyrics not found.")


def split_string_by_multiple_delimiters(string, delimiters):
    regex_pattern = "|".join(map(re.escape, delimiters))
    return re.split(regex_pattern, string)[0].strip()


def main():
    song_name, artist = get_currently_playing()

    if song_name and artist:
        song_name = split_string_by_multiple_delimiters(song_name, ["(", ")", "-"])

        print(get_lyrics(song_name, artist))
    else:
        print("No track is currently playing.")


if __name__ == "__main__":
    main()
