# TO CREATE INSTALLER
# pip install pyinstaller --break-system-packages
# python -m PyInstaller <file-name> --onefile --icon=<icon-name> -w

from tkinter import *
from tkinter import ttk
from time import sleep
import threading

###################################################################################################
ICON_PATH = './assets/icon.png'
###################################################################################################

root = Tk()

root.title("Titolo Finestra")
root.geometry(f"600x400")

imgicon = PhotoImage(file=f"{ICON_PATH}")
root.tk.call('wm', 'iconphoto', root._w, imgicon)

def longOperation():
    sleep(10)
    print("Long Operation")
def shortOperation():
    print("Short Operation")

button = Button(root, text="Long Operation", command= lambda:threading.Thread(target=longOperation).start() )
button.pack(expand=True, fill=X)

button = Button(root, text="Short Operation", command=shortOperation)
button.pack(expand=True, fill=X)

root.mainloop()