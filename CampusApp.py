import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os

screen = tk.Tk()

def search():
	
	searched = str(entry_box.get())
	print(searched)


# screen title and size
screen.title("Campus")
screen.geometry("930x610")

# What can be searched for
title_question = tk.Label(screen, text="Classes to Search:")
title_question.pack(side = TOP)


# Entry Box
entry_box = tk.Entry(screen)
entry_box.pack(side = TOP)

# Search Button
search_button = tk.Button(screen, text="Search", bg="Blue",command=search)
search_button.pack()
search_button.place(x = 550, y = 20)

img = ImageTk.PhotoImage(Image.open("campus.png"))
panel = tk.Label(screen, image = img)
panel.pack(side = BOTTOM)


screen.mainloop()
