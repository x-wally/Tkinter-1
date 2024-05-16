from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

###################################################################################################
ICON_PATH = './assets/icon.png'
###################################################################################################

root = Tk()

root.title("Titolo Finestra")
root.geometry(f"600x400")

imgicon = PhotoImage(file=f"{ICON_PATH}")
root.tk.call('wm', 'iconphoto', root._w, imgicon)

def apri_file():
    filetypes = ( ("File di testo", "*.txt"),("Tutti i File", "*.*") )
    
    filename = filedialog.askopenfilename(title="Apri un File", initialdir="/home/", filetypes=filetypes)
    
    f = open(filename, "r")
    data = f.read()
    print(data)
    f.close()

    f = open(filename, "w")
    data = "hello 1\nhello 2\nhello 3"
    f.write(data)
    f.close()

button = Button(root, text="Apri File", command=apri_file)
button.pack(expand=True)



root.mainloop()