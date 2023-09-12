import whisper
from googletrans import Translator
from gtts import gTTS
import os


def transcribe_audio(input_audio_file):
    model = whisper.load_model("small")
    result = model.transcribe(input_audio_file)
    return result["text"]


def translate_audio_and_synthesize(input_audio_file, target_language, output_audio_file):
    transcribed_text = transcribe_audio(input_audio_file)
    
   
    translator = Translator()
    translated_text = translator.translate(transcribed_text, dest=target_language).text
    
   
    tts = gTTS(translated_text, lang="fr")
    
    
    tts.save(output_audio_file)


input_audio_file = "C:/Users/HP/Desktop/dhoni.mp3"
target_language = "ru"
output_audio_file = "D:/Pipeline/dhonirussia.mp3"

translate_audio_and_synthesize(input_audio_file, target_language, output_audio_file)
