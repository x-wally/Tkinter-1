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

frame = ttk.Frame(root)
frame.pack(fill=BOTH, expand=True)

label = ttk.Label(frame, text="Label", background="orange")
label.pack()

# Menu ##########################################
contextMenu = Menu(root, tearoff=0)
contextMenu.add_command(label="Option 1")
contextMenu.add_command(label="Option 2")
contextMenu.add_command(label="Option 3")
contextMenu.add_separator()
contextMenu.add_command(label="Option 4")
contextMenu.add_command(label="Option 5")
#################################################

def contextMenuPopup(event):
    try:
        contextMenu.tk_popup(x=event.x_root,y=event.y_root)
    finally:
        contextMenu.grab_release()

frame.bind("<Button-3>", contextMenuPopup)

root.mainloop()