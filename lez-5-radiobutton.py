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

genere = StringVar()
r1 = Radiobutton(root, text="maschio", value="m", variable=genere)
r1.pack()
r2 = Radiobutton(root, text="femmina", value="f", variable=genere)
r2.pack()

button1 = Button(root, text="prova", command=lambda: print(genere.get()) )
button1.pack()

taglia_selezionata = StringVar()
taglie = (
    ("Small","S"),
    ("Medium","M"),
    ("Large","L"),
    ("Extra Large","XL")
)
for taglia in taglie:
    r = ttk.Radiobutton(root, text=taglia[0], value=taglia[1], variable=taglia_selezionata)
    r.pack(padx=5, pady=5)
button2 = Button(root, text="prova", command=lambda: print(taglia_selezionata.get()) )
button2.pack()


root.mainloop()