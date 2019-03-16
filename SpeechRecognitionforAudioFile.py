import speech_recognition as sr
from tkinter.filedialog import askopenfilename
from tkinter import Tk
def callback():
    Tk().withdraw()
    name=askopenfilename(initialdir="/",title="Select file",filetypes = (("audio files","*.wav"),("All files","*.*")))
    return name
f_name=callback()
r=sr.Recognizer()
hard=sr.AudioFile(f_name)
text=''
with hard as source:
    audio=r.record(source)
    try:
        text=r.recognize_google(audio)
        text_fname=str(input('Enter the text file name you want the transcript to be saved in:'))
        with open(text_fname,'w') as fd:
            fd.write(text)
    except:
        print("Error!")
    
