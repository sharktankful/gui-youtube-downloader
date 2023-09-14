from pytube import YouTube

def download_video(url):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download("downloads")

if __name__ == "__main__":
    video_url = input("Enter the URL of the YouTube video: ")
    download_video(video_url)
