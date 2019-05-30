import speech_recognition as sr
from tkinter.filedialog import askopenfilename
from tkinter import Tk
def callback():
    Tk().withdraw()
    name= askopenfilename(initialdir = "/",title = "Select file",filetypes = (("mp4 files","*.mp4"),("All files","*.*")))
    return name    
from moviepy.editor import *
try:
    f_name=callback()
except:
    print('Incorrect fileName')
video=VideoFileClip(f_name)
audio=video.audio
audio_fname=str(input('Enter the audio file name you want to save the audio in:')) 
audio.write_audiofile(audio_fname)
r=sr.Recognizer()
hard=sr.AudioFile(audio_fname)
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
        
