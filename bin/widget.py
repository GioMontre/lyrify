import tkinter as tk
from tkinter import messagebox
import threading
import time
import lyrics_getter as lg


class SpotifyWidget:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x100")
        self.label = tk.Label(root, text="Loading...")
        self.label.pack(pady=20)
        self.root.bind("<Button-1>", self.on_click)

    def update_song(self, song_name, artist_name):
        self.label.config(text=f"{song_name} by {artist_name}")

    def on_click(self, event):
        lyrics = self.get_lyrics()
        messagebox.showinfo("Lyrics", lyrics)

    def get_lyrics(self):
        # Call your existing lyrics fetching function
        song_name, artist_name = lg.get_currently_playing()
        lyrics = lg.get_lyrics(song_name, artist_name)
        return lyrics


def update_widget(widget):
    while True:
        song_name, artist_name = lg.get_currently_playing()
        if song_name:
            widget.update_song(song_name, artist_name)
        time.sleep(10)


root = tk.Tk()
widget = SpotifyWidget(root)

thread = threading.Thread(target=update_widget, args=(widget,))
thread.daemon = True
thread.start()

root.mainloop()
