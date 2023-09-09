from pytube import YouTube

url = input("Please enter the URL of the YouTube video you want to download: ")

yt = YouTube(url)

stream = yt.streams.get_highest_resolution()

output_path = "downloads"

stream.download(output_path)
