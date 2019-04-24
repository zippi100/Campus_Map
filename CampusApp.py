import tkinter as tk
from tkinter import *
import webbrowser


screen = tk.Tk()
canvas = tk.Canvas(screen)
canvas.pack(fill=tk.BOTH, expand=1)
floors_file = open("Floors.txt", "r")
floors = []
for line in floors_file:
	floors.append(line.rstrip())
floors_file.close()


def hyperlink(event):
	webbrowser.open_new(event.widget.cget("text"))


def search():
	flag = False
	floor_info = ""
	info_text.place_forget()

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
			not_valid.place(x=716, y=25)

	if selection.get() == "E":
		canvas.coords(info_box, 364, 340, 560, 416)
		fluff_text.place(x=405, y=377)
		link_text.config(text=r"http://www.fullerton.edu/ecs/")
		link_text.place(x=365, y=395)
		canvas.coords(highlight_circle, 570, 350, 620, 400)
		if flag:
			info_text.config(text=entry_box.get() + " is on the " + floor_info)
			info_text.place(x=389, y=341)

	elif selection.get() == "CS":
		canvas.coords(info_box, 406, 360, 602, 436)
		fluff_text.place(x=447, y=397)
		link_text.config(text=r"http://www.fullerton.edu/ecs/")
		link_text.place(x=407, y=415)
		canvas.coords(highlight_circle, 612, 370, 662, 420)
		if flag:
			info_text.config(text=entry_box.get() + " is on the " + floor_info)
			info_text.place(x=431, y=361)

	elif selection.get() == "EC":
		canvas.coords(info_box, 254, 364, 450, 440)
		fluff_text.place(x=295, y=401)
		link_text.config(text=r"http://hhd.fullerton.edu/")
		link_text.place(x=271, y=419)
		canvas.coords(highlight_circle, 460, 374, 530, 444)
		if flag:
			info_text.config(text=entry_box.get() + " is on the " + floor_info)
			info_text.place(x=279, y=365)

	elif selection.get() == "GH":
		canvas.coords(info_box, 184, 430, 380, 506)
		fluff_text.place(x=225, y=467)
		link_text.config(text=r"http://www.fullerton.edu/aac/")
		link_text.place(x=185, y=485)
		canvas.coords(highlight_circle, 390, 440, 440, 490)
		if flag:
			info_text.config(text=entry_box.get() + " is on the " + floor_info)
			info_text.place(x=209, y=431)

	elif selection.get() == "Hum":
		canvas.coords(info_box, 214, 400, 410, 476)
		fluff_text.place(x=255, y=437)
		link_text.config(text=r"http://hss.fullerton.edu/")
		link_text.place(x=231, y=455)
		canvas.coords(highlight_circle, 420, 400, 490, 470)
		if flag:
			info_text.config(text=entry_box.get() + " is on the " + floor_info)
			info_text.place(x=239, y=401)

	elif selection.get() == "LH":
		canvas.coords(info_box, 420, 450, 616, 526)
		fluff_text.place(x=461, y=487)
		link_text.config(text=r"http://vpadmin.fullerton.edu/")
		link_text.place(x=421, y=505)
		canvas.coords(highlight_circle, 330, 450, 410, 530)
		if flag:
			info_text.config(text=entry_box.get() + " is on the " + floor_info)
			info_text.place(x=445, y=451)

	elif selection.get() == "MH":
		canvas.coords(info_box, 390, 400, 590, 476)
		fluff_text.place(x=433, y=437)
		link_text.config(text=r"http://www.fullerton.edu/nsm/")
		link_text.place(x=391, y=455)
		canvas.coords(highlight_circle, 300, 406, 380, 486)
		if flag:
			info_text.config(text=entry_box.get() + " is on the " + floor_info)
			info_text.place(x=415, y=401)


# screen title and size
screen.title("Campus")
screen.geometry("930x610")

# What can be searched for
title_question = tk.Label(screen, text="Classes to Search:")
title_question.place(x=401, y=0)

# Campus image
campus_map = tk.PhotoImage(file="campus.png")
img = canvas.create_image(0, 100, anchor=tk.NW, image=campus_map)

# Highlight circle
highlight_circle = canvas.create_oval(0, 0, 0, 0, outline="Red", width=3)

# Entry Box
Label(screen, text="Room #(OPTIONAL):").place(x=438, y=25)
entry_box = tk.Entry(screen, width=6)
entry_box.place(x=580, y=25)

# Search Button
search_button = tk.Button(screen, text="Search", bg="Blue", command=search)
search_button.place(x=638, y=20)

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
fluff_text = Label(screen, bg="#adadad", text="Building website:")
link_text = Label(screen, bg="#adadad", fg="blue", cursor="hand2")
link_text.bind("<Button-1>", hyperlink)

# Building highlight


# Error text
not_valid = tk.Label(screen, text="Invalid room #")

screen.mainloop()
