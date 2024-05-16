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

notebook = ttk.Notebook(root)
notebook.pack(pady=10, fill=BOTH, expand=True)

frame1 = ttk.Frame(notebook, width=400, height=280)
frame1.pack(fill=BOTH, expand=True)
label = Label(frame1, text="Ciao").pack()
notebook.add(frame1, text="tab1")

frame2 = ttk.Frame(notebook, width=400, height=280)
frame2.pack(fill=BOTH, expand=True)
label = Label(frame2, text="Hello").pack()
notebook.add(frame2, text="tab2")

root.mainloop()