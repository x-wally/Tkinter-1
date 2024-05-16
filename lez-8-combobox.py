from tkinter import *
from tkinter import ttk
from calendar import month_name

###################################################################################################
ICON_PATH = './assets/icon.png'
###################################################################################################

root = Tk()

root.title("Titolo Finestra")
root.geometry(f"600x400")

imgicon = PhotoImage(file=f"{ICON_PATH}")
root.tk.call('wm', 'iconphoto', root._w, imgicon)

mese_selezionato = StringVar()
mesi = ttk.Combobox(root,
                    textvariable=mese_selezionato,

       )
mesi["values"] = [month_name[m] for m in range(1,13)]
mesi["state"] = "readonly"
mesi.pack(fill=X, padx=5, pady=5)

def seleziona_mese(event):
    print(f"mese selezionato: {mese_selezionato.get()}")

mesi.bind("<<ComboboxSelected>>", seleziona_mese)

root.mainloop()