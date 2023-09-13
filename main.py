'''
def main():
    record()
    recognizer()
    input()


if __name__ == '__main__':
    main()
'''

from record_to_file import record
from voice_recognizer import speech_recognition
from tkinter import *
from tkinter import ttk

def record_voice():
    seconds = text_window.get()
    try:
        seconds = int(seconds.strip())
        record_canvas.create_oval(5, 5, 45, 45, fill='red')
        root.update()
        record(seconds)
        record_canvas.delete("all")
    except:
        pass

def recognize_voice():
    global rtext
    model = view.get()
    speech_recognition(model)
    with open(f'transcription_{model}.txt',  'r') as file:
        rtext = [row for row in file][0]
    rtext_window.delete('1.0', END)
    rtext_window.insert('end', rtext)


root = Tk()
root.geometry('1200x700')
root.configure(bg='white')

record_label = Label(root, text='Запись', font=('Calibri', 70), bg='white')
record_label.place(x=30, y=0)
seconds_label = Label(root, text='время записи', font=('Calibri', 30), bg='white')
seconds_label.place(x=30, y=120)
text_window = Entry(root, font=('Calibri', 20))
text_window.place(x=30, y=180)
photo = PhotoImage(file = r"record_button.png") 
record_button = Button(root, image=photo, command=record_voice)
record_button.place(x=30, y=300)
record_canvas = Canvas(root, width = 50, height = 50, bg='white', highlightbackground = 'white')
record_canvas.place(x=340, y=370)

choose_model_label = Label(root, text='выбери модель обработки звука', font=('Calibri', 20), bg='white')
choose_model_label.place(x=500, y=0)
view = ttk.Combobox(root, values=['tiny', 'base', 'small', 'medium', 'large'])
view.place_configure(x = 900, y = 10)
view.set('small')
text_label = Label(root, text='Текст записи', font=('Calibri', 30), bg='white')
text_label.place(x = 500, y=50)
recognize_button = Button(root, text='Распознать', command=recognize_voice)
recognize_button.place(x=800, y=70)
rtext_window = Text(root)
rtext_window.place(x=500, y=100)

root.mainloop()
