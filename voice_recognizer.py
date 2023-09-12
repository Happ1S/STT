import os
import whisper


def speech_recognition(model='base'):
   speech_model = whisper.load_model(model)
   result = speech_model.transcribe("voice.wav")
   os.remove("voice.wav")
   with open(f'transcription_{model}.txt',  'w') as file:
      file.write(result['text'])
   print('----------------------------------------------------------------------------------------\n\n')
   with open(f'transcription_{model}.txt',  'r') as file:
      for row in file:
         print(row)
   print('\n\n----------------------------------------------------------------------------------------')


def recognizer():
   models = {1 : 'tiny', 2 : 'base', 3 : 'small', 4 : 'medium', 5 : 'large'}

   for k, v in models.items():
         print(f'{k} : {v}')
   
   model = int(input('выберите модель: '))

   if model not in models.keys():
      exit()
   else:
      print('Запуск...')
   speech_recognition(model=models[model])
