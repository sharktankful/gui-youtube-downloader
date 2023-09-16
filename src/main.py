from tqdm import tqdm
from pytube import YouTube

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

    # Create a tqdm progress bar
    pbar = tqdm(total=stream.filesize)

    # Define a callback function to update the progress bar
    def on_progress(stream, chunk, bytes_remaining):
        pbar.update(len(chunk))

    # Add the on_progress function to the yt instance
    yt.register_on_progress_callback(on_progress)

    # Download the video with the progress bar callback
    stream.download("downloads")

    # Close the progress bar
    pbar.close()

if __name__ == "__main__":
    video_url = input("Enter the URL of the YouTube video: ")
    download_video(video_url)
