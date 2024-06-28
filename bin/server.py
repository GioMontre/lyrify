import lyrics_getter as lg
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route("/")
def lyrics_page():

    song_name, artist_name = lg.get_currently_playing_song()
    if song_name:
        lyrics = lg.get_lyrics(song_name, artist_name)
        return render_template(
            "./lyrics_template.html",
            song_name=song_name,
            artist_name=artist_name,
            lyrics=lyrics,
        )


if __name__ == "__main__":
    app.run()
