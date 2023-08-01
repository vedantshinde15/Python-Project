from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
import speech_recognition as sr
import pyttsx3

root=Tk()
root.geometry('740x400')
root.title('Translator project')

def show():
    c1=comb1.get()
    c2=comb2.get()
    lab1.config(text=c1)
    lab2.config(text=c2)
    root.after(1000,show)

def translate():
    trans=Translator()
    transl=trans.translate(text1.get(1.0,END),src=comb1.get(),dest=comb2.get())
    text2.delete(1.0,END)
    text2.insert(END,transl.text)
             
def clear():
    text1.delete(1.0,END)
    text2.delete(1.0,END)

def exite():
    root.destroy()

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        text1.delete(1.0, END)
        text1.insert(END, text)
    except sr.UnknownValueError:
        messagebox.showwarning("Error", "Could not understand the audio.")
    except sr.RequestError:
        messagebox.showwarning("Error", "Failed to get results from Google Speech Recognition.")

def speak_output():
    text = text2.get(1.0, END)
    engine = pyttsx3.init()
    engine.setProperty("rate", 150) 
    engine.setProperty("volume", 2.0)  
    engine.say(text)
    engine.runAndWait()

voice_input_btn = Button(root, text='🎤', command=get_voice_input, font=('arial 20'), bd=0, bg='white', cursor='hand2')
voice_input_btn.place(x=350, y=120)

speech_output_btn = Button(root, text='🔊', command=speak_output, font=('arial 20'), bd=0, bg='white', cursor='hand2')
speech_output_btn.place(x=350, y=200)


language=list(LANGUAGES.values())


comb1=ttk.Combobox(root,values=language)
comb1.place(x=90,y=80)
comb1.set('English')

lab1=Label(root,text='English',font=('arial 20 ','30','bold'),bg='white',fg='#5582f9')
lab1.place(x=90,y=30)


lab2=Label(root,text='Hindi',font=('arial 20  ','30','bold'),bg='#5582f9',fg='white')
lab2.place(x=500,y=35)
comb2=ttk.Combobox(root,values=language)
comb2.place(x=500,y=80)
comb2.set('Hindi')

text1=Text(root,height=10,width=35,bg='#5582f9',fg='white',wrap=WORD)
text1.place(x=30,y=100)

text2=Text(root,height=10,width=35,bg='white',fg='#5582f9')
text2.place(x=430,y=100)


translate=Button(root,text='Translate',command=translate,font=('arial 20'),bd=0, bg='white',cursor='hand2')
translate.place(x=100,y=300)


clear=Button(root,text='Clear',command=clear,font=('arial 20 ','20'),bd=0,bg='#5582f9',cursor='hand2')
clear.place(x=325,y=300)


ext=Button(root,text='Exit',command=exite,font=('arial 20'),bd=0,bg='#5582f9',cursor='hand2')
ext.place(x=530,y=300)
show()

root.mainloop()