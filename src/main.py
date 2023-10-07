from pytube import YouTube
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
from pytube import YouTube

PATH = os.getcwd() + "\downloads"


def get_path():
    global PATH
    PATH = filedialog.askdirectory()
    filepath.config(text=PATH)


def bar():
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
        progress['value'] += (100*len(chunk))/fileSize
        window.update()
    

    yt.register_on_progress_callback(on_progress)

    stream.download(PATH)

    download_success.config(text="DOWNLOAD SUCCESS! ", font=("Arial", 18, "bold"), fg="green")
    


if __name__ == "__main__":
    window = Tk()
    window.title("Youtube Downloader")
    window.minsize(450, 150)
    

    label = Label(text="Enter the URL of the YouTube video: ")
    label.grid(row=0, column=0)

    video_url = Entry(width=60)
    video_url.focus()
    video_url.grid(row=0, column=1)

    url = video_url.get()
    download = Button(text="Download", command=bar)
    download.grid(row=0, column=2, padx=10, pady=10)

    filepath_label = Label(text="Downloading Path: ")
    filepath_label.grid(row=1, column=0)

    filepath = Label(text=f"{PATH}")
    filepath.grid(row=1, column=1)

    browse = Button(text="Change Path", command=get_path)
    browse.grid(row=1, column=2, padx=10, pady=10)

    progress = ttk.Progressbar(window, orient=HORIZONTAL,length=430, mode='determinate')
    progress.grid(row=2, column=0, columnspan=3,padx=20, pady=20, sticky=EW)

    download_success = Label(text="")
    download_success.grid(row=3, column=1, sticky="nw")

    window.mainloop()
