import os
import whisper


def speech_recognition(model='base'):
   speech_model = whisper.load_model(model)
   result = speech_model.transcribe("voice.wav")
   # os.remove("voice.wav")
   with open(f'transcription_{model}.txt',  'w') as file:
      file.write(result['text'])
      