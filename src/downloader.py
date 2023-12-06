from pytube import YouTube
from pytube.exceptions import VideoUnavailable, RegexMatchError

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from ttkthemes import ThemedTk

import os

PATH = os.path.join(os.getcwd(), "downloads")

def gui():
    """
    Graphical User Interface for downloading YouTube videos.
    """

    print("\nGUI running...")

    def get_path():
        """
        Open a dialog to choose the download path and update the GUI label.
        """
        
        global PATH
        PATH = filedialog.askdirectory()
        filepath_label.config(text=PATH)

    def download_video():
        """
        Download the YouTube video when the 'Download' button is clicked.
        """

        url = video_url_entry.get()

        try:
            yt = YouTube(url)
            window.update()
            stream = yt.streams.get_highest_resolution()
            fileSize = stream.filesize

            def on_progress(stream, chunk, bytes_remaining):
                """
            Callback function to update the download progress bar.

            Args:
                stream (pytube.Stream): The stream being downloaded.
                chunk (bytes): The chunk of data being downloaded.
                bytes_remaining (int): The number of bytes remaining to download.
            """
                downloaded_bytes = fileSize - bytes_remaining
                download_progressbar['value'] = int((downloaded_bytes / fileSize) * 100)
                window.update()

            yt.register_on_progress_callback(on_progress)

            stream.download(PATH)
            download_status_label.config(text="DOWNLOAD SUCCESS!", fg="green")
            
        except VideoUnavailable:
            messagebox.showerror(title="ERROR!", message="The Provided Video is unavailable")
            
        except RegexMatchError:
            messagebox.showerror(title="ERROR!", message="Provided URL is either empty or invalid, please verify and try again.")

    window = ThemedTk(theme="breeze")
    window.title("YouTube Downloader")

    url_message_label = tk.Label(text="Enter the URL of the YouTube video:")
    url_message_label.grid(row=0, column=0, padx=15, pady=10)

    video_url_entry = tk.Entry(width=60)
    video_url_entry.grid(row=0, column=1, padx=15, pady=10)
    video_url_entry.focus()

    download_button = tk.Button(text="Download", command=download_video, width=25)
    download_button.grid(row=0, column=2, padx=15, pady=10)

    filepath_message_label = tk.Label(text="Downloading Path:")
    filepath_message_label.grid(row=1, column=0)

    filepath_label = tk.Label(text=PATH)
    filepath_label.grid(row=1, column=1)

    browse_button = tk.Button(text="Change Path", command=get_path, width=25)
    browse_button.grid(row=1, column=2, padx=15, pady=10)

    download_progressbar = ttk.Progressbar(window, mode='determinate')
    download_progressbar.grid(row=2, column=0, padx=15, pady=10, columnspan=3, sticky="ew")

    download_status_label = tk.Label(text="")
    download_status_label.grid(row=3, column=2, padx=15, pady=10)

    window.mainloop()

    print("The window has been closed.\n")