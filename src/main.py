import time

from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable

from tkinter import filedialog, messagebox

import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.grid_columnconfigure((0, 1, 2), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # line 1

        self.label1 = customtkinter.CTkLabel(self, text="Enter the URL of the YouTube video:")
        self.label1.grid(row=0, column=0, padx=15, pady=10)

        self.entry1 = customtkinter.CTkEntry(self, width=350)
        self.entry1.grid(row=0, column=1, padx=15, pady=10)

        self.button1 = customtkinter.CTkButton(self, text="Download", width=150)
        self.button1.grid(row=0, column=2, padx=15, pady=10)
        self.button1.configure(command=self.download_video)

        # line 2

        self.label2 = customtkinter.CTkLabel(self, text="Downloading Path:")
        self.label2.grid(row=1, column=0, padx=15, pady=10)

        self.label3 = customtkinter.CTkLabel(self, text="PATH")
        self.label3.grid(row=1, column=1, padx=15, pady=10)

        self.button2 = customtkinter.CTkButton(self, text="Change path", width=150)
        self.button2.grid(row=1, column=2, padx=15, pady=10)
        self.button2.configure(command=self.change_path)

        # line 3

        self.progress_bar = customtkinter.CTkProgressBar(self, mode="determinate")
        self.progress_bar.grid(row=2, column=0, padx=15, pady=10, columnspan=3, sticky="ew")
        self.progress_bar.set(0)

        # line 4

        self.label4 = customtkinter.CTkLabel(self, text="Status")
        self.label4.grid(row=3, column=2, padx=15, pady=10)

    def download_video(self):
        url = self.entry1.get()

        try:
            video = YouTube(url)

            stream = video.streams.get_highest_resolution()

            self.label4.configure(text="Downloading...")

            def on_progress(stream, chunk, bytes_remaining):
                downloaded_bytes = stream.filesize - bytes_remaining
                self.progress_bar.set(downloaded_bytes / stream.filesize)
                self.progress_bar.update()

            video.register_on_progress_callback(on_progress)

            stream.download("downloads/")

            self.label4.configure(text="DOWNLOAD SUCCESS!")
            self.label4.update()

            time.sleep(3)

            self.progress_bar.set(0)
            self.label4.configure(text="Status")

        except RegexMatchError:
            messagebox.showerror(
                title="ERROR!",
                message="Provided URL is either empty or invalid, please verify and try again."
            )

        except VideoUnavailable:
            messagebox.showerror(
                title="ERROR!",
                message="The provided video is unavailable."
            )

    def change_path(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
