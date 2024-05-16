from tkinter import *
from tkinter import ttk

###################################################################################################
ICON_PATH = './assets/icon.png'
IMAGE_PATH = './assets/image.png'
###################################################################################################

root = Tk()

root.title("Titolo Finestra")
root.geometry(f"600x400")

imgicon = PhotoImage(file=f"{ICON_PATH}")
root.tk.call('wm', 'iconphoto', root._w, imgicon)

photo = PhotoImage(file=f"{IMAGE_PATH}")

label = Label (root, 
               text="Ciao!\nSono Wally",
               background="blue",
               padx=50, pady=50,
               foreground="white", # colore testo
               font=("Helvetica",24),
               cursor="pirate", 
               justify="left", # allineamento testo
               image=photo,
               compound="top"  # top(=immagine sopra),
                               # bottom (=immagine sotto),
                               # left(=immagine a sinistra), 
                               # right(=immagine a destra), 
                               # none(=mostro testo solo se non c'è immagine) 
        )
label.pack()

root.mainloop()