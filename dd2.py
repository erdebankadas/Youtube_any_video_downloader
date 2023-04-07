from pytube import YouTube

# paste the YouTube video link
link = "https://www.youtube.com/watch?v=l8jcSwlh7bo"

# create a YouTube object
yt = YouTube(link)

# get all streams
streams = yt.streams.all()

# select the streams with both video and audio
streams = [s for s in streams if s.mime_type == "video/mp4" and s.includes_audio_track]

# download all streams
for stream in streams:
    print("Downloading:", stream)
    stream.download()
