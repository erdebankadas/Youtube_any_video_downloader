from django.shortcuts import render
from django.http import HttpResponse
from .forms import VideoForm
from pytube import YouTube

def download_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            # get the video link from the form data
            link = form.cleaned_data['link']

            # create a YouTube object
            yt = YouTube(link)

            # get all streams
            streams = yt.streams.all()

            # select the streams with both video and audio
            streams = [s for s in streams if s.mime_type == "video/mp4" and s.includes_audio_track]

            # download all streams
            for stream in streams:
                # get the file path to download the stream
                file_path = stream.download()

                # open the file and read the content
                with open(file_path, 'rb') as f:
                    file_content = f.read()

                # create the HTTP response object with the video content
                response = HttpResponse(file_content, content_type='video/mp4')
                response['Content-Disposition'] = 'attachment; filename="video.mp4"'

                return response
    else:
        form = VideoForm()
    return render(request, 'download.html', {'form': form})

# from django.shortcuts import render
# from django.http import HttpResponse
# from .forms import VideoForm
# from pytube import YouTube

# def download_video(request):
#     if request.method == 'POST':
#         form = VideoForm(request.POST)
#         if form.is_valid():
#             # get the video link from the form data
#             link = form.cleaned_data['link']

#             # create a YouTube object
#             yt = YouTube(link)

#             # get all streams
#             streams = yt.streams.all()

#             # select the streams with both video and audio
#             streams = [s for s in streams if s.mime_type == "video/mp4" and s.includes_audio_track]

#             # download all streams
#             for stream in streams:
#                 # get the file path to download the stream
#                 file_path = stream.download()

#                 # open the file and read the content
#                 with open(file_path, 'rb') as f:
#                     file_content = f.read()

#                 # create the HTTP response object with the video content
#                 response = HttpResponse(file_content, content_type='video/mp4', status=200, reason=None, charset=None, headers={'Content-Disposition': 'attachment; filename="video.mp4"', 'X-Frame-Options': 'SAMEORIGIN'})
#                 return response
#     else:
#         form = VideoForm()
#     return render(request, 'download.html', {'form': form})
