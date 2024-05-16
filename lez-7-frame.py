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

labelframe = LabelFrame(root, text="LABELFRAME", background="yellow", padx=10, pady=50, height=100, width=400)
labelframe.pack(fill=BOTH, expand=True)

frame1 = Frame(labelframe,
              background="red",
              padx=10, pady=50,
              height=100, width=400
        )
frame1.pack(fill=BOTH, expand=True)
#frame1.pack()

frame2 = Frame(labelframe,
              background="purple",
              padx=10, pady=50,
              height=100, width=400
        )
frame2.pack(fill=BOTH, expand=True)
#frame2.pack()

frame3 = Frame(labelframe,
              background="green",
              padx=10, pady=50,
              height=100, width=400
        )
frame3.pack(fill=BOTH, expand=True)
#frame3.pack()

button = Button(frame1, text="Ciao!")
button.pack()
button = Button(frame2, text="Ciao!")
button.pack()
button = Button(frame3, text="Ciao!")
button.pack()

root.mainloop()