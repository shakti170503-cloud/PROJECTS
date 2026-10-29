from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog

def video_download(url, save_path):
    try:
        yt = YouTube(url)
        print(f"Video Title: {yt.title}")

        stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()

        if stream is None:
            print("Could not find a downloadable MP4 stream!")
            return

        stream.download(output_path=save_path)
        print("Video Downloaded Successfully!!!")

    except Exception as e:
        print(f"Download failed: {e}")

def open_file():
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory(title="Select download folder")
    root.destroy()
    return folder

if __name__ == "__main__":
    video_url = input("Paste your URL here: ").strip()

    save_dir = open_file()

    if save_dir:
        print("Starting download...")
        video_download(video_url, save_dir)
    else:
        print("Invalid file location!")