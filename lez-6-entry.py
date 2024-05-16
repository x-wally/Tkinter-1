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

email_label = ttk.Label(root, text="Email: ")
email_label.pack(padx=5, pady=5)

email = StringVar()
email_entry = ttk.Entry(root, textvariable=email)
email_entry.pack(padx=5, pady=5)
email_entry.focus()

password_label = ttk.Label(root, text="Password: ")
password_label.pack(padx=5, pady=5)

password = StringVar()
password_entry = ttk.Entry(root, textvariable=password, show="*")
password_entry.pack(padx=5, pady=5)

def login():
    print(f"Login({email.get()},{password.get()})")

button = ttk.Button(root, text="Login", command=login)
button.pack()

root.mainloop()