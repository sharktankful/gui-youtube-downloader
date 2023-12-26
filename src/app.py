import os
import time

from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable

from tkinter import filedialog, messagebox

import customtkinter

from tabview import TabView

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):
    """
    A YouTube video downloader application using customtkinter and Pytube.
    """

    def __init__(self):
        """
        Initialize the application window.
        """

        super().__init__()

        self.download_path = os.path.join(os.getcwd(), "downloads")

        self.title("YouTube Downloader")

        self.tabview = TabView(master=self)
        self.tabview.grid(row=0, column=0, padx=20, pady=30)

    def download_video(self):
        """
        Download the YouTube video specified by the provided URL.
        """

        url = self.tabview.url_entry.get()

        try:
            video = YouTube(url)

            stream = video.streams.get_highest_resolution()

            self.tabview.status_label.configure(text="Downloading...")

            def on_progress(stream, chunk, bytes_remaining):
                """
                Callback function to update the download progress bar.

                Args:
                    stream (pytube.Stream): The stream being downloaded.
                    chunk (bytes): The chunk of data being downloaded.
                    bytes_remaining (int): The number of bytes remaining to download.
                """

                downloaded_bytes = stream.filesize - bytes_remaining
                self.tabview.progress_bar.set(downloaded_bytes / stream.filesize)
                self.tabview.progress_bar.update()

            video.register_on_progress_callback(on_progress)

            stream.download(self.download_path)

            self.tabview.status_label.configure(text="DOWNLOAD SUCCESS!")
            self.tabview.status_label.update()

            time.sleep(3)

            self.tabview.progress_bar.set(0)
            self.tabview.status_label.configure(text="Status")

        except RegexMatchError:
            messagebox.showerror(
                title="ERROR",
                message="Provided URL is either empty or invalid, please verify and try again."
            )

        except VideoUnavailable:
            messagebox.showerror(
                title="ERROR",
                message="The provided video is unavailable."
            )

    def change_path(self):
        """
        Change the download path by opening a directory selection dialog.
        """

        self.download_path = filedialog.askdirectory()

        if self.download_path == "":
            self.download_path = os.path.join(os.getcwd(), "downloads")

        self.tabview.path_label2.configure(text=self.download_path)
        self.tabview.path_label2.update()
