from pytube import YouTube
from tqdm import tqdm

import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

import os


class Downloader:
    @staticmethod
    def cli():
        """
        Command Line Interface for downloading YouTube videos.
        """

        def download_video(url):
            """
            Download a video from a given YouTube URL with a progress bar using tqdm.

            Args:
                url (str): The URL of the YouTube video to be downloaded.
            """

            yt = YouTube(url)

            stream = yt.streams.get_highest_resolution()
            pbar = tqdm(total=stream.filesize, unit="B", unit_scale=True, colour="red")

            def on_progress(stream, chunk, bytes_remaining):
                """
                Callback function to update the progress bar.

                Args:
                    stream (pytube.Stream): The stream being downloaded.
                    chunk (bytes): The chunk of data being downloaded.
                    bytes_remaining (int): The number of bytes remaining to download.
                """

                pbar.update(len(chunk))

            yt.register_on_progress_callback(on_progress)
            stream.download("downloads/")

            pbar.close()
            print("Download successfully completed!\n")

        video_url = input("\nEnter the URL of the YouTube video: ")
        download_video(video_url)

    @staticmethod
    def gui():
        """
        Graphical User Interface for downloading YouTube videos.
        """

        print("\nGUI running...")

        path = os.path.join(os.getcwd(), "downloads/")

        def download_video():
            """
            Download the YouTube video when the 'Download' button is clicked.
            """

            url = video_url.get()

            yt = YouTube(url)

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

            stream.download(path)
            download_status.config(text="DOWNLOAD SUCCESS!", fg="green")

        window = ThemedTk(theme="breeze")
        window.title("YouTube Downloader")
        window.minsize(939, 126)

        label = tk.Label(text="Enter the URL of the YouTube video:")
        label.grid(row=0, column=0, padx=15, pady=10)

        video_url = tk.Entry(width=60)
        video_url.grid(row=0, column=1, padx=15, pady=10)
        video_url.focus()

        download_button = tk.Button(text="Download", command=download_video, width=25)
        download_button.grid(row=0, column=2, padx=15, pady=10)

        progress = ttk.Progressbar(window, mode='determinate')
        progress.grid(row=1, column=0, padx=15, pady=10, columnspan=3, sticky="ew")

        download_status = tk.Label(text="")
        download_status.grid(row=2, column=2, padx=15, pady=10)

        window.mainloop()

        print("The window has been closed.\n")
