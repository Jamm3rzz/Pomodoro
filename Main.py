import time
from pygame import mixer
import tkinter as tk
from tkinter import ttk
from tkinter import *

bgColor = "#11bbdd"
textColor = "#002233"
highlightColor = "#33ffff"

mixer.init()
mixer.music.load(r'C:\Users\James\Documents\Mikubot\.venv\Include\Assets\taco-bell-bong-sfx.mp3')
root = tk.Tk()
root.title("study")
root.geometry("600x400")
backgroundImage = tk.PhotoImage(file=r"C:\Users\James\Desktop\Projects\Pomodoro\.venv\Include\Assets\Untitled design.png")
icon = tk.PhotoImage(file=r"C:\Users\James\Desktop\Projects\Pomodoro\.venv\Include\Assets\taco.png")
root.iconphoto(False, icon)
sweetSpot = 0
waitOrPlay = False

def FlippingHourGlass(WaitTime):
    global sweetSpot, waitOrPlay
    if WaitTime <= 0: 
        sweetSpot = 0
        mixer.music.play()
        if waitOrPlay: # Time play
            timePlayVal = int(timePlay.get()) * 60
            progressBar["maximum"] = timePlayVal
            progressBar["value"] = sweetSpot
            waitOrPlay = False
            FlippingHourGlass(timePlayVal)
        else: # Time work 
            timeWorkVal = int(timeWork.get()) * 60
            progressBar["maximum"] = timeWorkVal
            progressBar["value"] = sweetSpot
            waitOrPlay = True
            FlippingHourGlass(timeWorkVal)
    else:
        sweetSpot += 1
        progressBar['value'] = sweetSpot
        root.after(1000, lambda: (FlippingHourGlass(WaitTime - 1)))

def Sizing(amount: int) -> None: 
    for x in range(amount):
        root.grid_columnconfigure(x, minsize=10 ,weight = 1)
        frame = tk.Frame(root, background='')
        frame.grid(row = 0, column = x, sticky = "nsew")
        frame.grid_propagate(False)
        for i in range(amount):
            root.grid_rowconfigure(i, minsize=10, weight = 1)
            frame = tk.Frame(root, background='')
            frame.grid(row = i, column = x, sticky = "nsew")
            frame.grid_propagate(False)

background = tk.Label(root, image=backgroundImage)
background.place(x=-2, y=-2)

Sizing(5)

textColor = tk.Canvas()



#title = tk.Label(root, textColor="Focus on your task", background=bgColor, foreground=textColor)
#title.grid(row=0, column=2) # --

start = tk.Button(root, background=bgColor, foreground=textColor, command=lambda: FlippingHourGlass(0)) # lambda is for handing functions as a VALUE to be used later as opposed to them being called that moment. Like handing a note on how to do smth instead of doing it when asked.
#start.grid(row=4, column=1) # --

#workLabel = tk.Label(root, textColor="Work time: ", background=bgColor, foreground=textColor)
#workLabel.grid(row=2, column=1) # --

timeWork = ttk.Entry(root, background=bgColor, foreground=textColor)
#timeWork.grid(row=2, column=2) # --

#playLabel = tk.Label(root, textColor="Play time: ", background=bgColor, foreground=textColor)
#playLabel.grid(row=3, column=1) # --

timePlay = ttk.Entry(root, background=bgColor, foreground=textColor)
#timePlay.grid(row=3, column=2) # --

progressBar = ttk.Progressbar(root, orient="horizontal", mode="determinate", length=300)

#progressBar.grid(row=4, column=2) # --

progressBar['maximum'] = None
progressBar['value'] = None #

root.mainloop()