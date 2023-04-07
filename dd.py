from pytube import YouTube

# paste the YouTube video link
link = "https://www.youtube.com/watch?v=l8jcSwlh7bo"
# link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# create a YouTube object
yt = YouTube(link)

# get the first stream, which is usually the highest resolution stream
stream = yt.streams.first()
# select the streams with both video and audio
# streams = [s for s in streams if s.mime_type == "video/mp4" and s.includes_audio_track]


# download the video to the current working directory
stream.download()
