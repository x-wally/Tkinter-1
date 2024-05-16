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

'''
padx : spazio fuori a destra e sinistra
pady : spazio fuori sopra e sotto

ipadx : spazio dentro destra e sinistra
ipady : spazio dentro sopra e sotto

from calendar import month_name
fill=X : riempi spazio a destra/sinistra se ce n'è
fill=Y : riempi spazio sopra e sotto se ce n'è
fill=BOTH : riempi in tutte le direzioni se può

expand=True : prende tutto lo spazio possibile nel contenitore

side : [LEFT,RIGHT,TOP,BOTTOM]
'''

label1 = Label(root, text= "Label1", background="yellow", foreground="black")
label1.pack(padx=10, pady=50)
label2 = Label(root, text= "Label2", background="orange", foreground="black")
label2.pack(ipadx=20, ipady=20)

root.mainloop()