from pytube import YouTube

def download_video():
    url = input("Enter the URL of the YouTube video: ")
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    output_path = "downloads"
    stream.download(output_path)

if __name__ == "__main__":
    download_video()
