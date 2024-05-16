from tkinter import *
from tkinter import ttk
from tkinter import messagebox

###################################################################################################
ICON_PATH = './assets/icon.png'
IMAGE_PATH = './assets/image.png'
###################################################################################################

root = Tk()

root.title("Titolo Finestra")
root.geometry(f"600x400")

imgicon = PhotoImage(file=f"{ICON_PATH}")
root.tk.call('wm', 'iconphoto', root._w, imgicon)

def info():
    print( messagebox.showinfo(title="Info", message="Info message") )
def warning():
    print( messagebox.showwarning(title="Warning", message="Warning message") )
def error():
    print( messagebox.showerror(title="Error", message="Error message") )
def askokcancel():
    print( messagebox.askokcancel(title="AskOkCancel", message="AskOkCancel message") )
def askquestion():
    print( messagebox.askquestion(title="AskQuestion", message="AskQuestion message") )
def askretrycancel():
    print( messagebox.askretrycancel(title="AskRetryCancel", message="AskRetryCancel") )
def askyesno():
    print( messagebox.askyesno(title="AskYesNo", message="AskYesNo") )
def askyesnocancel():
    print( messagebox.askyesnocancel(title="AskYesNoCancel", message="AskYesNoCancel") )

button1 = ttk.Button(root, text="Mostra Messaggio Info", command=info)
button1.pack()
button2 = ttk.Button(root, text="Mostra Messaggio Warning", command=warning)
button2.pack()
button3 = ttk.Button(root, text="Mostra Messaggio Error", command=error)
button3.pack()
button4 = ttk.Button(root, text="Mostra Messaggio AskOkCancel", command=askokcancel)
button4.pack()
button5 = ttk.Button(root, text="Mostra Messaggio AskQuestion", command=askquestion)
button5.pack()
button6 = ttk.Button(root, text="Mostra Messaggio AskRetryCancel", command=askretrycancel)
button6.pack()
button7 = ttk.Button(root, text="Mostra Messaggio AskYesNo", command=askyesno)
button7.pack()
button8 = ttk.Button(root, text="Mostra Messaggio AskYesNoCancel", command=askyesnocancel)
button8.pack()

root.mainloop()