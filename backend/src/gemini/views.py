from django.shortcuts import render
from django.http import JsonResponse
from pytube import YouTube
import os
import assemblyai as aai

def my_json_view(request):
    return JsonResponse("Hello World", safe=False)


def yt_transcript(request, video_url):
    URL = "https://www.youtube.com/watch?" + video_url
    yt = YouTube(video_url)
    stream = yt.streams.filter(only_audio=True).first()
    download_path = stream.download()
    
    # Check if the output file already exists and remove it if it does
    if os.path.exists("audio_file.wav"):
        os.remove("audio_file.wav")
    
    # Rename the downloaded file to the output file
    os.rename(download_path, "audio_file.wav")

    aai.settings.api_key = "c94c0d628b434b6c8f3d50e97f90a09f"
    transcriber = aai.Transcriber()

    transcript = transcriber.transcribe("./audio_file.wav")

    return JsonResponse(transcript.text, safe=False)