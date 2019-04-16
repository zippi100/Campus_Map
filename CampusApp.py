import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os


screen = tk.Tk()
canvas = tk.Canvas(screen)
canvas.pack(fill=tk.BOTH, expand=1)
floors_file = open("Floors.txt", "r")
floors = []
for line in floors_file:
	floors.append(line.rstrip())
floors_file.close()


def search():
	flag = False
	floor_info = ""

	if entry_box.get() is not "":
		for x in range(0, len(floors)):
			if selection.get() == floors[x].split('	', 1)[0]:
				while floors[x] != "," and flag is not True:
					x += 1
					if entry_box.get() == floors[x]:
						flag = True
						not_valid.place_forget()
						while len(floors[x].split(' ', 2)) != 2:
							x -= 1
						floor_info = floors[x].replace(':', '')

		if not flag:
			not_valid.place(x=645, y=25)
	print(selection.get())
	if selection.get() == "E":
		if flag:
			canvas.coords(info_box, 440, 240, 620, 380)
			info_text.config(text=entry_box.get() + " is on the " + floor_info)
			info_text.place(x=456, y=241)
	elif selection.get() == "CS":
		if flag:
			canvas.coords(info_box, 470, 270, 650, 410)
			info_text.config(text=entry_box.get() + " is on the " + floor_info)
			info_text.place(x=486, y=271)
	elif selection.get() == "EC":
		print("True")
	elif selection.get() == "GH":
		print("")
	elif selection.get() == "Hum":
		print("")
	elif selection.get() == "LH":
		print("")
	elif selection.get() == "MH":
		print("")


# screen title and size
screen.title("Campus")
screen.geometry("930x610")

# What can be searched for
title_question = tk.Label(screen, text="Classes to Search:")
title_question.place(x=401, y=0)

# Campus image
campus_map = tk.PhotoImage(file="campus.png")
img = canvas.create_image(0, 100, anchor=tk.NW, image=campus_map)

# Entry Box
Label(screen, text="Room #:").place(x=438, y=25)
entry_box = tk.Entry(screen, width=6)
entry_box.place(x=500, y=25)

# Search Button
search_button = tk.Button(screen, text="Search", bg="Blue", command=search)
search_button.place(x=558, y=20)

# Dropdown menu
Label(screen, text="Building Initials:").place(x=252, y=25)
buildings = ["E", "CS", "EC", "GH", "Hum", "LH", "MH"]
selection = StringVar(screen)
selection.set(buildings[0])
buildings_dropdown = OptionMenu(screen, selection, *buildings)
buildings_dropdown.config(width=3)
buildings_dropdown.place(x=360, y=20)

# Information box
info_box = canvas.create_rectangle(0, 0, 0, 0, fill="#adadad")
info_text = Label(screen, bg="#adadad")

# Building highlight


# Error text
not_valid = tk.Label(screen, text="Invalid room #")

screen.mainloop()
