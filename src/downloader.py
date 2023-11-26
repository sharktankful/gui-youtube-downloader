import os
import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import ttk
from ttkthemes import ThemedTk
from pytube import YouTube

# Default download path
PATH = os.path.join(os.getcwd(), "downloads")

def gui():
    """
    Graphical User Interface for downloading YouTube videos.
    """

    print("\nGUI running...")

    def get_path():
        """Open a dialog to choose the download path and update the GUI label."""
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

        stream.download(PATH)
        download_status.config(text="DOWNLOAD SUCCESS!", fg="green")
        

            

    window = ThemedTk(theme="breeze")
    window.title("YouTube Downloader")
    window.minsize(450, 150)

    label = tk.Label(text="Enter the URL of the YouTube video:")
    label.grid(row=0, column=0, padx=10)

    video_url = tk.Entry(width=60)
    video_url.focus()
    video_url.grid(row=0, column=1)

    download = tk.Button(text="Download", command=download_video)
    download.grid(row=0, column=2, padx=10, pady=10)

    filepath_label = tk.Label(text="Downloading Path:")
    filepath_label.grid(row=1, column=0)

    filepath = tk.Label(text=PATH)
    filepath.grid(row=1, column=1)

    browse = tk.Button(text="Change Path", command=get_path)
    browse.grid(row=1, column=2, padx=10, pady=10)

    progress = ttk.Progressbar(window, orient="horizontal", length=430, mode='determinate')
    progress.grid(row=2, column=0, columnspan=3, padx=20, pady=20, sticky="ew")

    download_status = tk.Label(text="")
    download_status.grid(row=3, column=2, padx=15, pady=10)

    window.mainloop()

    print("The window has been closed.\n")