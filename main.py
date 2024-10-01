from tkinter import *
import ctypes
import re
import os

previousText = ""
keys = ["void", "int", "bool"]

def rgb(rgb):
    return "#%02x%02x%02x" % rgb

def onUpdateSyntax(event):
    global previousText
    
    lines = editArea.get("1.0", END).splitlines()
    
    if previousText == editArea.get("1.0", END):
        return None
    
    editArea.tag_delete("code")
    editArea.tag_delete("comment")
    editArea.tag_configure("code", foreground=keywords)
    editArea.tag_configure("comment", foreground=comments)
    
    # Set code colors
    i = 1
    for line in lines:
        pattern = r"\b(" + "|".join(keys) + r")\b"
        matches = [(match, line.find(match)) for match in re.findall(pattern, line)]
        for match, pos in matches:
            editArea.tag_add("code", str(i) + "." + str(pos), str(i) + "." + str(pos + len(match)))
        
        if line.find("//") != -1:
            start_pos = re.search("//", line).start()
            end_pos = start_pos + len(line)
            if start_pos != -1:
                editArea.tag_add("comment", str(i) + "." + str(start_pos), str(i) + "." + str(end_pos))
    
        i += 1
    
    previousText = editArea.get("1.0", END)

def onEditText(event):
    onUpdateSyntax(event)
        

ctypes.windll.shcore.SetProcessDpiAwareness(True)

root_window = Tk()

root_window.title("Lumin Code")
root_window.geometry("1280x720")


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
editArea.config(tabs="1.2c")
editArea.insert("1.0", "// Welcome to Lumin Code! \n" +
                "// Start write your code.")

editArea.bind("<KeyRelease>", onEditText)
editArea.bind("<Control-l>", onUpdateSyntax)

root_window.mainloop()