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

def premo_check():
    print(f"valore : {valoreCheck.get()}")
    label = Label(root, text=valoreCheck.get())
    label.pack()

valoreCheck = StringVar()

check = Checkbutton (root, 
                     text="Ciao!", 
                     font=("Helvetica", 24), 
                     command=premo_check, 
                     onvalue="attivo",
                     offvalue="disattivo",
                     variable=valoreCheck
        )
check.pack()

root.mainloop()