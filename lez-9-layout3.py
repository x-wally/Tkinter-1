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

label1 = Label(root, text= "Label1", background="yellow", foreground="black")
label1.pack(fill=X,ipadx=10,ipady=10)
label2 = Label(root, text= "Label2", background="orange", foreground="black")
label2.pack(fill=X,ipadx=10,ipady=10)
label3 = Label(root, text= "Label3", background="pink", foreground="black")
label3.pack(fill=X,ipadx=10,ipady=10)

label4 = Label(root, text= "Label4", background="lightblue", foreground="black")
label4.pack(fill=BOTH, expand=True, side=LEFT)
label5 = Label(root, text= "Label5", background="lightgreen", foreground="black")
label5.pack(fill=BOTH, expand=True, side=LEFT)
label6 = Label(root, text= "Label6", background="purple", foreground="black")
label6.pack(fill=BOTH, expand=True, side=LEFT)

root.mainloop()