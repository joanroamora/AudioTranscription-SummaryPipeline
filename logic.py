import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
import subprocess
from transformers import pipeline
import vosk
import wave
import json

def audio_converter(video_path):
    audio_path = "./audio/audio.wav"
    
    # Extraer el audio usando moviepy
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    temp_audio_path = "./audio/temp_audio.wav"
    audio_clip.write_audiofile(temp_audio_path, codec='pcm_s16le')

    audio_clip.close()
    video_clip.close()

    # Usar ffmpeg para convertir el archivo a mono y PCM
    final_audio_path = "./audio/audio.wav"
    command = [
        "ffmpeg", "-i", temp_audio_path,
        "-ac", "1",  # Convertir a mono
        "-ar", "16000",  # Configurar la tasa de muestreo a 16 kHz
        "-acodec", "pcm_s16le",  # Configurar el codec a PCM 16-bit
        final_audio_path
    ]
    subprocess.run(command, check=True)

    # Verificar el formato del archivo exportado
    with wave.open(final_audio_path, "rb") as wf:
        channels = wf.getnchannels()
        sample_width = wf.getsampwidth()
        comp_type = wf.getcomptype()
        if channels != 1 or sample_width != 2 or comp_type != "NONE":
            raise ValueError("Audio file was not converted to WAV format mono PCM.")

    # Eliminar el archivo temporal
    os.remove(temp_audio_path)
    
    return final_audio_path

def audio_to_text(audio_path):
    model_path = "/home/elgado/Desktop/Proyectos/audio a texto/1.Youtube-resume-vid-audio-text-pipeline/models/vosk-model-es-0.42"
    model = vosk.Model(model_path)

    wf = wave.open(audio_path, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        raise ValueError("Audio file must be WAV format mono PCM.")
    
    recognizer = vosk.KaldiRecognizer(model, wf.getframerate())
    text = ""

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            text += json.loads(result)["text"] + " "
        else:
            partial_result = recognizer.PartialResult()
            text += json.loads(partial_result)["partial"] + " "

    transcription_path = "./transcriptions/transcription.txt"
    with open(transcription_path, "w") as file:
        file.write(text)
    
    return transcription_path

def text_transformers_resume(transcription_path):
    summarizer = pipeline("summarization")
    
    with open(transcription_path, "r") as file:
        text = file.read()
    
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
    
    summary_path = "./resumes/summary.txt"
    with open(summary_path, "w") as file:
        file.write(summary)
    
    return summary_path

def print_screen(summary_path):
    with open(summary_path, "r") as file:
        summary = file.read()
    
    # Devolver el resumen para imprimirlo en la interfaz
    return summary

# Llamada de prueba a la función
audio_to_text("./audio/audio.wav")
