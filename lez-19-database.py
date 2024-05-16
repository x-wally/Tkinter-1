from tkinter import *
from tkinter import ttk
import psycopg2

###################################################################################################
ICON_PATH = './assets/icon.png'
###################################################################################################

root = Tk()

root.title("Titolo Finestra")
root.geometry(f"600x400")

imgicon = PhotoImage(file=f"{ICON_PATH}")
root.tk.call('wm', 'iconphoto', root._w, imgicon)

conn = psycopg2.connect("dbname=postgres user=postgres")
curs = conn.cursor()

curs.execute("SELECT * FROM tabella")
rslt = curs.fetchall()
print(rslt)

colonne = ("id","email","username","password")
tabella = ttk.Treeview(root, columns=colonne, show="headings")
tabella.heading("id", text="Id")
tabella.heading("email", text="Email")
tabella.heading("username", text="Username")
tabella.heading("password", text="Password")
[tabella.insert('', END, values=riga) for riga in rslt]
tabella.grid(row=0, column=0, sticky="news")

def aggiorna_tabella():
    for row in tabella.get_children():
        tabella.delete(row)

    curs.execute("SELECT * FROM tabella")
    rslt = curs.fetchall()
    for riga in rslt:
        tabella.insert('', END, values=riga)

def inserisci():
    sql = 'INSERT INTO tabella(id,email,username,password) VALUES (%s,%s,%s,%s)'
    val = ("1","email@test.com","user1","pass1")
    curs.execute(sql,val)
    conn.commit()
    aggiorna_tabella()

def modifica():
    sql = "UPDATE tabella SET email = 'email@test.it' WHERE id = 1"
    curs.execute(sql)
    conn.commit()
    aggiorna_tabella()

def elimina():
    sql = 'DELETE FROM tabella WHERE id = 1'
    curs.execute(sql)
    conn.commit()
    aggiorna_tabella()

BTN_inserisci = Button(root, text="Inserisci", command=inserisci).grid(row=1, column=0)
BTN_modifica = Button(root, text="Modifica", command=modifica).grid(row=2, column=0)
BTN_elimina = Button(root, text="Elimina", command=elimina).grid(row=3, column=0)

root.mainloop()