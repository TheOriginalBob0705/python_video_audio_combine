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

        self.output_clip = None

    def select_audio_file(self):
        self.audio_file_path = filedialog.askopenfilename(title="Select Audio File", filetypes=[("Audio Files", "*.mp3;*.wav")])

    def select_video_file(self):
        self.video_file_path = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video Files", "*.mp4")])

    def overlay_audio_video(self):
        if self.audio_file_path and self.video_file_path:
            audio_clip = AudioFileClip(self.audio_file_path)
            video_clip = VideoFileClip(self.video_file_path)

            # Overlay audio on video
            video_clip = video_clip.set_audio(audio_clip)

            self.output_clip = video_clip

    def save_output(self):
        if hasattr(self, 'output_clip'):
            output_path = filedialog.asksaveasfilename(title="Save Output File", defaultextension=".mp4", filetypes=[("Video Files", "*.mp4")])
            self.output_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")


if __name__ == "__main__":
    root = tk.Tk()
    app = AudioVideoOverlayApp(root)
    root.mainloop()
