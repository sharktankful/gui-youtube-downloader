from pytube import YouTube
from tqdm import tqdm

def download_video(url):
    """
    Download a video from a given YouTube URL with a progress bar using tqdm.

    Args:
        url (str): The URL of the YouTube video to be downloaded.

    Returns:
        None
    """

    # Create a YouTube object for the given URL
    yt = YouTube(url)

    # Get the highest resolution stream
    stream = yt.streams.get_highest_resolution()

    # Create a tqdm progress bar
    pbar = tqdm(total=stream.filesize, unit="B", unit_scale=True, colour="red")

    # Define a callback function to update the progress bar
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
        
        # Update the tqdm progress bar
        pbar.update(len(chunk))

    # Add the on_progress function to the yt instance
    yt.register_on_progress_callback(on_progress)

    # Download the video with the progress bar callback
    stream.download("downloads")

    # Close the progress bar
    pbar.close()

    # Print a message to say that the download has been successfully completed
    print("Download successfully completed!")

if __name__ == "__main__":
    # Prompt the user to enter the URL of the YouTube video
    video_url = input("Enter the URL of the YouTube video: ")

    # Call the download_video function with the provided URL
    download_video(video_url)
