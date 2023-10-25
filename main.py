import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pytube import YouTube
from tqdm import tqdm

# Define the default download path
PATH = os.path.join(os.getcwd(), "downloads")

def cli():
    """Command Line Interface for downloading YouTube videos."""
    
    def download_video(url):
        """
        Download a video from a given YouTube URL with a progress bar using tqdm.

        Args:
            url (str): The URL of the YouTube video to be downloaded.

        Returns:
            None
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

            Returns:
                None
            """
            pbar.update(len(chunk))

        yt.register_on_progress_callback(on_progress)
        stream.download("downloads")
        pbar.close()
        print("Download successfully completed!")

    video_url = input("Enter the URL of the YouTube video: ")
    download_video(video_url)

def gui():
    """Graphical User Interface for downloading YouTube videos."""
    
    def get_path():
        """Open a dialog to choose the download path and update the GUI label."""
        global PATH
        PATH = filedialog.askdirectory()
        filepath.config(text=PATH)

    def download_video():
        """Download the YouTube video when the 'Download' button is clicked."""
        progress['value'] = 0
        download_success.config(text="")
        window.update()

        url = video_url.get()

        try:
            yt = YouTube(url)
        except:
            messagebox.showerror(title="ERROR!", message="Provided URL is either empty or invalid, please verify and try again.")

        window.update()
        stream = yt.streams.get_highest_resolution()
        fileSize = stream.filesize

        def on_progress(stream, chunk, bytes_remaining):
            """Callback function to update the download progress bar."""
            downloaded_bytes = fileSize - bytes_remaining
            progress['value'] = int((downloaded_bytes / fileSize) * 100)
            window.update()

        yt.register_on_progress_callback(on_progress)

        stream.download(PATH)
        download_success.config(text="DOWNLOAD SUCCESS!", font=("Arial", 18, "bold"), fg="green")

    window = tk.Tk()
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

    download_success = tk.Label(text="")
    download_success.grid(row=3, column=1, sticky="w")

    window.mainloop()

exit_status = False

while exit_status == False:
    choice = input("Welcome to YouTube Downloader!\n"
                   "Enter 1 for Command Line Interface\n"
                   "Enter 2 for Graphical User Interface\n"
                   "Enter 'exit' to Exit\n"
                   "Enter your input: ")

    if choice == "1":
        cli()  # Call the cli function
    elif choice == "2":
        gui()  # Call the gui function
    elif choice.lower() == "exit":
        exit_status = True
