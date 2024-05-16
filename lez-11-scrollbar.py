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
root.rowconfigure(0, weight=1)

linguaggi = [
    "L1","L2","L3","L4","L5",
    "L6","L7","L8","L9","L10",
    "L11","L12","L13","L14","L15",
    "L16","L17","L18","L19","L20",
    "L1","L2","L3","L4","L5",
    "L6","L7","L8","L9","L10",
    "L11","L12","L13","L14","L15",
    "L16","L17","L18","L19","L20",
]

linguaggio_selezionato = StringVar(value=linguaggi)

listbox = Listbox(root,
                  listvariable=linguaggio_selezionato,
                  height=6,
                  selectmode="extended"
          )
listbox.grid(row=0, column=0, sticky="nwes")

scrollbar = ttk.Scrollbar(root, orient="vertical", command=listbox.yview)
scrollbar.grid(row=0,column=1, sticky="ns")

listbox["yscrollcommand"] = scrollbar.set

root.mainloop()