import os
import pygame
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageDraw, ImageTk

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x300")
        
        self.current_song_label = tk.Label(root, text="Currently Playing:", font=("Helvetica", 12))
        self.current_song_label.pack(pady=10)
        
        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.play_button.pack(pady=5)
        
        self.pause_button = tk.Button(root, text="Pause", command=self.pause_music)
        self.pause_button.pack(pady=5)
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=5)
        
        self.select_button = tk.Button(root, text="Select Song", command=self.select_music)
        self.select_button.pack(pady=10)
        
        self.forward_button = tk.Button(root, text="Forward 5s", command=self.forward_music)
        self.forward_button.pack(pady=5)
        
        self.backward_button = tk.Button(root, text="Backward 5s", command=self.backward_music)
        self.backward_button.pack(pady=5)
        
        self.music_file = None
        self.playing = False    
        
    def play_music(self):
        if self.music_file:
            pygame.mixer.init()
            pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.play()
            self.playing = True
            self.update_current_song_label()
    
    def pause_music(self):
        if self.playing:
            pygame.mixer.music.pause()
            self.playing = False
    
    def stop_music(self):
        if self.playing:
            pygame.mixer.music.stop()
            self.playing = False
            self.update_current_song_label()
    
    def select_music(self):
        self.music_file = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        self.update_current_song_label()
    
    def forward_music(self):
        if self.playing:
            current_time = pygame.mixer.music.get_pos() / 1000
            new_time = current_time + 5
            pygame.mixer.music.set_pos(new_time)
    
    def backward_music(self):
        if self.playing:
            current_time = pygame.mixer.music.get_pos() / 1000
            new_time = max(0, current_time - 5)
            pygame.mixer.music.set_pos(new_time)
    
    def update_current_song_label(self):
        if self.music_file:
            song_name = os.path.basename(self.music_file)
            self.current_song_label.config(text=f"Currently Playing: {song_name}")
        else:
            self.current_song_label.config(text="Currently Playing: ")

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
