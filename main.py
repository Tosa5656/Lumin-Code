from tkinter import *
import ctypes
import re
import os

def rgb(rgb):
    return "#%02x%02x%02x" % rgb

def onEditText(event):
    pass

ctypes.windll.shcore.SetProcessDpiAwareness(True)

root_window = Tk()

root_window.title("Lumin Code")
root_window.geometry("1280x720")


previousText = ""

normal = rgb((234, 234, 234))
keywords = rgb((234, 95, 95))
comments = rgb((95, 234, 16))
string = rgb((234, 162, 95))
function = rgb((95, 211, 234))
background = rgb((42, 42, 42))

font = "Consolas 15"

editArea = Text(
    root_window, background=background, foreground=normal, insertbackground=normal, relief=FLAT, borderwidth=30, font=font
)

editArea.pack(fill=BOTH, expand=1)
editArea.insert("1.0", "// Welcome to Lumin Code! \n" +
                "// Start write your code.")

editArea.tag_configure("code", foreground=keywords)

editArea.bind("<KeyRelease>", onEditText)

root_window.mainloop()