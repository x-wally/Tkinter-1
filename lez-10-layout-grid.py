from tkinter import *
from tkinter import ttk

###################################################################################################
ICON_PATH = './assets/icon.png'
###################################################################################################

root = Tk()

root.title("Titolo Finestra")
root.geometry(f"600x400")

imgicon = PhotoImage(file=f"{ICON_PATH}")
root.tk.call('wm', 'iconphoto', root._w, imgicon)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

frame1 = Frame(root, background="yellow", height=200, width=200)
frame2 = Frame(root, background="orange", height=200, width=200)
frame3 = Frame(root, background="pink", height=200, width=200)
frame4 = Frame(root, background="red", height=200, width=200)

frame1.grid(row=0,column=0, columnspan=2)
#frame2.grid(row=0,column=1)
frame3.grid(row=1,column=0)
frame4.grid(row=1,column=1)

root.mainloop()