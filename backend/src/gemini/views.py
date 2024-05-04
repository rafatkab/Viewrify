from django.shortcuts import render
from django.http import JsonResponse
from pytube import YouTube
import os
import assemblyai as aai
import requests
from django.http import JsonResponse
from django.urls import path
from .views import google_speech_to_text, gemini_nlp
import os
from google.cloud import speech_v1
from django.http import JsonResponse

def my_json_view(request):
    return JsonResponse("Hello World", safe=False)


def yt_transcript(video_url, output_file):
    yt = YouTube(video_url)
    stream = yt.streams.filter(only_audio=True).first()
    download_path = stream.download()
    
    # Check if the output file already exists and remove it if it does
    if os.path.exists(output_file):
        os.remove(output_file)
    
    # Rename the downloaded file to the output file
    os.rename(download_path, output_file)

    aai.settings.api_key = "c94c0d628b434b6c8f3d50e97f90a09f"
    transcriber = aai.Transcriber()

    transcript = transcriber.transcribe("./audio_file.wav")

    return JsonResponse(transcript.text)



def gemini_nlp(request):
    if request.method == 'POST' and 'text' in request.POST:
        text = request.POST['text']
        headers = {
            'Authorization': 'Bearer AIzaSyAOm7I0NqpmhaguHO_I390doFkFVVg5p9k',
            'Content-Type': 'application/json'
        }
        data = {'text': text}

        response = requests.post('https://api.gemini.ai/v1/analyze', headers=headers, json=data)

        if response.status_code == 200:
            analysis = response.json()
            return JsonResponse({'analysis': analysis})
        else:
            return JsonResponse({'error': 'GeminiAI request failed.'})
    else:
        return JsonResponse({'error': 'Invalid request method or no text provided.'})


urlpatterns = [
    path('google-speech-to-text/', google_speech_to_text, name='google_speech_to_text'),
    path('gemini-nlp/', gemini_nlp, name='gemini_nlp'),
    # Other URL patterns
]


def google_speech_to_text(request):
    if request.method == 'POST' and request.FILES['audio_file']:
        audio_file = request.FILES['audio_file']

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/your/google_credentials.json"
        client = speech_v1.SpeechClient()

        content = audio_file.read()
        audio = speech_v1.RecognitionAudio(content=content)
        config = speech_v1.RecognitionConfig(
            encoding=speech_v1.RecognitionConfig.AudioEncoding.LINEAR16,
            language_code="en-US",
        )

        response = client.recognize(config=config, audio=audio)

        transcripts = []
        for result in response.results:
            transcripts.append(result.alternatives[0].transcript)

        return JsonResponse({'transcripts': transcripts})
    else:
        return JsonResponse({'error': 'Invalid request method or no audio file provided.'})
