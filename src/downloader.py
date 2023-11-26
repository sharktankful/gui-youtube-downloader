from pytube import YouTube
import tkinter as tk

from tkinter import ttk, filedialog
from ttkthemes import ThemedTk

import os


PATH = os.path.join(os.getcwd(), "downloads")

def gui():
    """
    Graphical User Interface for downloading YouTube videos.
    """

    print("\nGUI running...")

    path = os.path.join(os.getcwd(), "downloads/")

    def get_path():
        """
        Open a dialog to choose the download path and update the GUI label.
        """
        
        global PATH
        PATH = filedialog.askdirectory()
        filepath.config(text=PATH)

    def download_video():
        """
        Download the YouTube video when the 'Download' button is clicked.
        """

        url = video_url.get()

        try:
            yt = YouTube(url)

        except:
            exit("\nThe URL you provided is either empty or invalid.")

        progress['value'] = 0
        download_status.config(text="Downloading...")
        window.update()

        stream = yt.streams.get_highest_resolution()
        file_size = stream.filesize

        def on_progress(stream, chunk, bytes_remaining):
            """
            Callback function to update the download progress bar.

            Args:
                stream (pytube.Stream): The stream being downloaded.
                chunk (bytes): The chunk of data being downloaded.
                bytes_remaining (int): The number of bytes remaining to download.
            """

            downloaded_bytes = file_size - bytes_remaining
            progress['value'] = int((downloaded_bytes / file_size) * 100)
            window.update()

        yt.register_on_progress_callback(on_progress)

        print(PATH)

        stream.download(PATH)
        download_status.config(text="DOWNLOAD SUCCESS!", fg="green")

    window = ThemedTk(theme="breeze")
    window.title("YouTube Downloader")

    label = tk.Label(text="Enter the URL of the YouTube video:")
    label.grid(row=0, column=0, padx=15, pady=10)

    video_url = tk.Entry(width=60)
    video_url.grid(row=0, column=1, padx=15, pady=10)
    video_url.focus()

    download_button = tk.Button(text="Download", command=download_video, width=25)
    download_button.grid(row=0, column=2, padx=15, pady=10)

    filepath_label = tk.Label(text="Downloading Path:")
    filepath_label.grid(row=1, column=0)

    filepath = tk.Label(text=PATH)
    filepath.grid(row=1, column=1)

    browse_button = tk.Button(text="Change Path", command=get_path, width=25)
    browse_button.grid(row=1, column=2, padx=15, pady=10)

    progress = ttk.Progressbar(window, mode='determinate')
    progress.grid(row=2, column=0, padx=15, pady=10, columnspan=3, sticky="ew")

    download_status = tk.Label(text="")
    download_status.grid(row=3, column=2, padx=15, pady=10)

    window.mainloop()

    print("The window has been closed.\n")
