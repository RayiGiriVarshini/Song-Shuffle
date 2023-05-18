import pygame
import random
import os
from tkinter import Tk, Button

class MusicPlayer:
    def __init__(self, playlist):
        self.playlist = playlist
        self.current_song = 0
        self.paused = False

        pygame.init()
        pygame.mixer.init()

        self.root = Tk()
        self.root.title("Music Player")
        self.root.geometry("300x100")

        self.stop_button = Button(self.root, text="Stop", command=self.stop)
        self.stop_button.pack(side="left")

        self.pause_button = Button(self.root, text="Pause", command=self.pause)
        self.pause_button.pack(side="left")

        self.resume_button = Button(self.root, text="Resume", command=self.resume)
        self.resume_button.pack(side="left")

        self.previous_button = Button(self.root, text="Previous", command=self.previous)
        self.previous_button.pack(side="left")

        self.next_button = Button(self.root, text="Next", command=self.next)
        self.next_button.pack(side="left")

    def play(self):
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            pygame.mixer.music.load(self.playlist[self.current_song])
            pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()
        self.paused = True

    def resume(self):
        pygame.mixer.music.unpause()
        self.paused = False

    def previous(self):
        self.current_song -= 1
        if self.current_song < 0:
            self.current_song = len(self.playlist) - 1
        self.play()

    def next(self):
        self.current_song += 1
        if self.current_song >= len(self.playlist):
            self.current_song = 0
        self.play()

    def shuffle_playlist(self):
        random.shuffle(self.playlist)

    def run(self):
        self.shuffle_playlist()
        self.play()
        self.root.mainloop()

# Specify the path to your song files
playlist = [
    "PRV audio files/song1audio.mp3",
    "PRV audio files/song2audio.mp3",
    "PRV audio files/song3audio.mp3",
    "PRV audio files/song4audio.mp3",
    "PRV audio files/song5audio.mp3",
    "PRV audio files/song6audio.mp3",
    "PRV audio files/song7audio.mp3",
    "PRV audio files/song8audio.mp3",
    "PRV audio files/song9audio.mp3",
    "PRV audio files/song10audio.mp3",
    "PRV audio files/song11audio.mp3",
    "PRV audio files/song12audio.mp3",
    "PRV audio files/song13audio.mp3",
    "PRV audio files/song14audio.mp3",
    "PRV audio files/song15audio.mp3",
    "PRV audio files/song16audio.mp3",
    "PRV audio files/song17audio.mp3",
    "PRV audio files/song18audio.mp3"
    "PRV audio files/song19audio.mp3",
    "PRV audio files/song20audio.mp3",                 
]

player = MusicPlayer(playlist)
player.run()

