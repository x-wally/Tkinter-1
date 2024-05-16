from tkinter import *
from tkinter import ttk

###################################################################################################
ICON_PATH = './assets/icon.png'
###################################################################################################

root = Tk()

root.title("Titolo Finestra")
root.geometry(f"700x400")

imgicon = PhotoImage(file=f"{ICON_PATH}")
root.tk.call('wm', 'iconphoto', root._w, imgicon)

colonne = ("nome","cognome","email")
tabella = ttk.Treeview(root, columns=colonne, show="headings")

tabella.heading("nome", text="Nome")
tabella.heading("cognome", text="Cognome")
tabella.heading("email", text="Email")

righe = []
for i in range(1,50):
    righe.append( (f"nome-{i}",f"cognome-{i}",f"email-{i}") )
for r in righe:
    tabella.insert("", END, values=r)

tabella.grid(row=0, column=0, sticky="news")

scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=tabella.yview)
scrollbar.grid(row=0, column=1, sticky="ns")

tabella.configure(yscrollcommand=scrollbar.set)

root.mainloop()