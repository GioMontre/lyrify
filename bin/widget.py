import lyrics_getter as lg


def main():
    song_name, artist_name = lg.get_currently_playing_song()
    if song_name:
        print(lg.get_lyrics(song_name, artist_name))


if __name__ == "__main__":
    main()
