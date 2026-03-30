import gtts
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
import os

def text_to_speech(message, user_id):
    file_name = f"tts_{user_id}.mp3"
    tts = gtts.gTTS(message, lang="en")
    tts.save(file_name)
    return file_name

def ogg_to_wav(ofn):
    wfn = ofn.replace(".ogg", ".wav")
    segment = AudioSegment.from_file(ofn)
    segment.export(wfn, format="wav")
    return wfn

def speech_to_text(ogg_filename):
    wav_filename = ogg_to_wav(ogg_filename)
    r = sr.Recognizer()
    try:
        with sr.AudioFile(wav_filename) as source:
             audio = r.record(source) # Читаем аудиофайл
             text = r.recognize_google(audio_data = audio)  # Распознаем через Google
             return text
    except Exception as e:
        return f"Ошибка распознавания: {e}"
    finally:
        if os.path.exists(wav_filename):
            os.remove(wav_filename)