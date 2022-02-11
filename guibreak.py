from tkinter import *
from tkinter import ttk
from playsound import playsound
import os
import secrets

songs = ["bell_boy.wav", "black.wav", "dance.wav", 
    "sedan.wav", "sunglasses.wav", "why.wav"]

#insert times remaining in listbox
def wait15():
    list1.insert(END,"15 minutes remaining")

def wait10():
    list1.insert(END,"10 minutes remaining")

def wait5():
    list1.insert(END,"5 minutes remaining")

def play_time():
    # for playing random music wav file
    playme = secrets.choice(songs)
    audio_file = os.path.dirname(__file__) + '/tunes/'+ playme
    playsound(audio_file)

def wake():
    #refresh screen and play music
    list1.delete(0,END)
    list1.insert(0,"PLAY TIME!!!")
    list1.after(100, play_time)

def study_time():
    #main timing function
    list1.delete(0,END)
    list1.insert(0 ,"Start study or project 20 minutes")
    list1.insert(END,"20 minutes remaining")
    list1.after(300000, wait15)
    list1.after(600000, wait10)
    list1.after(900000, wait5)
    list1.after(1200000, wake)
        
# create root window & title
root = Tk()
root.title('Take a Break')
root.geometry('355x455')

#create content frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# create listbox for output text
list1 = Listbox(root, height = 17, width = 30, foreground="green", background="black", font=(15))
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 3)

# create buttons
b1=Button(root, text = "Start", width=24, command= study_time)
b1.grid(row=10, column=0, sticky=W)

b2=Button(root, text = "Quit", width=24, command= root.destroy)
b2.grid(row=10, column=1,sticky=W,)

root.mainloop()

