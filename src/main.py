from pytube import YouTube

def download_video(url):
    """
    Download a video from a given YouTube URL.

    Args:
        url (str): The URL of the YouTube video to be downloaded.

    Returns:
        None
    """
    
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download("downloads")

if __name__ == "__main__":
    video_url = input("Enter the URL of the YouTube video: ")
    download_video(video_url)
