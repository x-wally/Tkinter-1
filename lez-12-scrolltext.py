from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

###################################################################################################
ICON_PATH = './assets/icon.png'
###################################################################################################

root = Tk()

root.title("Titolo Finestra")
root.geometry(f"600x400")

imgicon = PhotoImage(file=f"{ICON_PATH}")
root.tk.call('wm', 'iconphoto', root._w, imgicon)

scrolltxt = ScrolledText(root,width=50,height=10)
scrolltxt.pack(fill=BOTH, expand=True, side=LEFT)

root.mainloop()