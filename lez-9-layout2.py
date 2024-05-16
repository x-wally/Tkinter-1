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

label1 = Label(root, text= "Label1", background="lightgreen", foreground="black")
label1.pack(fill=BOTH, expand=True)
label2 = Label(root, text= "Label2", background="lightblue", foreground="black")
label2.pack(fill=BOTH, expand=True)

root.mainloop()