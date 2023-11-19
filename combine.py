import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip, AudioFileClip

class AudioVideoOverlayApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Audio Video Overlay")

        self.audio_file_path = None
        self.video_file_path = None

        # Create buttons
        self.audio_button = tk.Button(master, text="Select Audio File", command=self.select_audio_file)
        self.audio_button.pack(pady=10)

        self.video_button = tk.Button(master, text="Select Video File", command=self.select_video_file)
        self.video_button.pack(pady=10)

        self.overlay_button = tk.Button(master, text="Overlay", command=self.overlay_audio_video)
        self.overlay_button.pack(pady=10)

        self.save_button = tk.Button(master, text="Save", command=self.save_output)
        self.save_button.pack(pady=10)


