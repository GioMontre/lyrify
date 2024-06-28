"""
    Author: Giovanni Montresor
"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import lyricsgenius as lg
import re


def get_currently_playing_song() -> tuple[str, str]:
    """get_currently_playing_song."""

    try:
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
        song_name = clean_song_name(results["item"]["name"], ["(", ")", "-"])
        artist_name = results["item"]["artists"][0]["name"]
        if results:
            return song_name, artist_name
        else:
            return "Can't get currently playing.", "Can't get the artist."

    except Exception as e:
        print(f"Something went wrong: {e}")
        return "Can't get currently playing.", "Can't get the artist."


def get_lyrics(song_name: str, artist: str) -> str:
    """get_lyrics.
    function to get the lyrics of a song.
    :param song_name (str): song name to get the lyrics.
    :param artist (str): related artist (just one) to get the lyrics.
    :return (str): lyrics of the song.
    """
    try:
        load_dotenv()
        genius_id = os.getenv("GENIUS_ID")
        genius = lg.Genius(
            genius_id,
            skip_non_songs=True,
            excluded_terms=["(Remix)", "(Live)"],
        )

        song = genius.search_song(song_name, artist)
        if song:
            return song.lyrics
        else:
            return "Lyrics not found."

    except Exception as e:
        print(f"Something went wrong: {e}")
        return f"Something went wrong: {e}"


def clean_song_name(string: str, delimiters: list[str]) -> str:
    """clean_song_name.
    function to clean the song name from unwanted characters.
    :param string (str): string to clean from unwanted characters.
    :param delimiters (list[str, ...]):
    :return (str): cleaned string.
    """
    try:
        regex_pattern = "|".join(map(re.escape, delimiters))
        cleaned_string = re.split(regex_pattern, string)[0].strip()

        return cleaned_string

    except Exception as e:
        print(f"Something went wrong: {e}")
        return f"Something went wrong: {e}"


if __name__ == "__main__":
    print("Import this module as a library.")
    print(
        """ Here an example of how to use this module.

    song_name, artist = get_currently_playing_song()

    if song_name and artist:
        print(get_lyrics(song_name, artist))
    else:
        print("No track is currently playing.")
    """
    )
