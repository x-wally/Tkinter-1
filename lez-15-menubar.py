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

menubar = Menu(root, tearoff=0)
root.config(menu=menubar)

menu1 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Menu 1", menu=menu1)
menu1.add_command(label="Option 1", command=root.quit) # option
menu1.add_command(label="Option 2", command=root.quit) # option
menu1.add_separator() # separator
menu1.add_command(label="Option 3", command=root.quit) # option

menu2 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Menu 2", menu=menu2)
menu2.add_command(label="Option 1", command=root.quit) # option
menu2.add_command(label="Option 2", command=root.quit) # option
# sub-menu ########
submenu = Menu(menu2, tearoff=0)
menu2.add_cascade(label="Sub Menu", menu=submenu)
submenu.add_command(label="Sub Option 1", command=root.quit) # sub-option
submenu.add_command(label="Sub Option 2", command=root.quit) # sub-option
###################
menu2.add_command(label="Option 4", command=root.quit) # option

menu3 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Menu 3", menu=menu3)
menu3.add_command(label="Option 1", command=root.quit) # option
menu3.add_command(label="Option 2", command=root.quit) # option
menu3.add_command(label="Option 3", command=root.quit) # option

root.mainloop()