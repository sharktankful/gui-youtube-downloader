import os
import time

from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable

from tkinter import filedialog, messagebox


import customtkinter

from PIL import Image
import urllib.request

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):
    """
    A YouTube video downloader application using customtkinter and Pytube.
    """

    def __init__(self):
        """
        Initialize the application window and set up the UI components.
        """

        super().__init__()

        self.download_path = os.path.join(os.path.expanduser("~"), "Downloads")

        self.title("YouTube Downloader")

        # line 1

        self.url_status_label = customtkinter.CTkLabel(
            self, text="Enter the URL of the YouTube video:")
        self.url_status_label.grid(row=0, column=0, padx=15, pady=10)

        self.url_entry = customtkinter.CTkEntry(self, width=500)
        self.url_entry.grid(row=0, column=1, padx=15, pady=10)

        self.download_button = customtkinter.CTkButton(
            self, text="Download", width=150)
        self.download_button.grid(row=0, column=2, padx=15, pady=10)
        self.download_button.configure(command=self._download_video)

        # line 2

        self.path_label1 = customtkinter.CTkLabel(
            self, text="Downloading Path:")
        self.path_label1.grid(row=1, column=0, padx=15, pady=10)

        self.path_label2 = customtkinter.CTkLabel(
            self, text=self.download_path)
        self.path_label2.grid(row=1, column=1, padx=15, pady=10)

        self.change_path_button = customtkinter.CTkButton(
            self, text="Change path", width=150)
        self.change_path_button.grid(row=1, column=2, padx=15, pady=10)
        self.change_path_button.configure(command=self._change_path)

        # line 3

        self.progress_bar = customtkinter.CTkProgressBar(
            self, mode="determinate")
        self.progress_bar.grid(row=2, column=0, padx=15,
                               pady=10, columnspan=3, sticky="ew")
        self.progress_bar.set(0)

        # line 4

        self.status_label = customtkinter.CTkLabel(self, text="Status")
        self.status_label.grid(row=3, column=2, padx=15, pady=10)

    def _download_video(self):
        """
        Download the YouTube video specified by the provided URL.
        """

        url = self.url_entry.get()

        try:
            video = YouTube(url)

            # line 5 - YOUTUBE TITLE
            self.title_label = customtkinter.CTkLabel(
                self, text=f"Title: {video.title}")
            self.title_label.grid(row=4, column=0, padx=15, pady=10)

            # line 6 - THUMBNAIL IMAGE
            urllib.request.urlretrieve(video.thumbnail_url, "thumbnail")

            self.image = customtkinter.CTkImage(Image.open("thumbnail"), size=(426, 240))
            self.thumbnail = customtkinter.CTkLabel(self, text="", image=self.image)
            self.thumbnail.grid(row=5, column=0, padx=15, pady=10)


            stream = video.streams.get_highest_resolution()

            self.status_label.configure(text="Downloading...")

            def on_progress(stream, chunk, bytes_remaining):
                """
                Callback function to update the download progress bar.

                Args:
                    stream (pytube.Stream): The stream being downloaded.
                    chunk (bytes): The chunk of data being downloaded.
                    bytes_remaining (int): The number of bytes remaining to download.
                """

                downloaded_bytes = stream.filesize - bytes_remaining
                self.progress_bar.set(downloaded_bytes / stream.filesize)
                self.progress_bar.update()

            video.register_on_progress_callback(on_progress)

            stream.download(self.download_path)

            self.status_label.configure(text="DOWNLOAD SUCCESS!")
            self.status_label.update()

            time.sleep(3)

            self.progress_bar.set(0)
            self.status_label.configure(text="Status")

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

    def _change_path(self):
        """
        Change the download path by opening a directory selection dialog.
        """

        self.download_path = filedialog.askdirectory()

        if self.download_path == "":
            self.download_path = os.path.join(
                os.path.expanduser("~"), "Downloads")

        self.path_label2.configure(text=self.download_path)
        self.path_label2.update()
