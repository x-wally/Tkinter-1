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

def button_callback():
    print("Ho cliccato il bottone")

photo = PhotoImage(file=f"{IMAGE_PATH}")

# ttk Button
button1 = ttk.Button (root, 
                      text="Ciao!", 
                      width=20,
                      command=button_callback,
                      image=photo,
                      compound="left",
                      state="active"
          )
ttk.Style().configure("TButton", background="blue", foreground="white", borderwidth=3)
button1.pack(ipadx=20, ipady=20)

button1.state(["active"]) # active, normal, disabled

# tk Button
button2 = Button (root, 
                     text="Chiudimi", 
                     background="blue",
                     foreground="white",
                     width=20,
                     borderwidth=3,
                     command=lambda: root.quit() # funzione inline
          )
button2.pack()

button2["state"] = "normal" 

root.mainloop()