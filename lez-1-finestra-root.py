from tkinter import *
from tkinter import ttk

###################################################################################################

# TITOLO FINESTRA
WINDOW_TITLE = 'Window Title'

# LARGHEZZA FINESTRA
WIDTH = 600
# ALTEZZA FINESTRA
HEIGHT = 400
# DISTANZA DAL BORDO SINISTRO
X = 50
# DISTANZA DAL BORDO DESTRO
Y = 50

# PATH ICONA
ICON_PATH = './assets/icon.png'

# LARGHEZZA MINIMA FINESTRA
MIN_SIZE_X = 400
# ALTEZZA MINIMA FINESTRA
MIN_SIZE_Y = 200
# LARGHEZZA MASSIMA FINESTRA
MAX_SIZE_X = 800
# ALTEZZA MASSIMA FINESTRA
MAX_SIZE_Y = 600

# TRASPARENZA FINESTRA (1.0 -> 0.0)
''' doesn't work '''
ALPHA = 1
# FINESTRA IN FULLSCREEN
FULLSCREEN = False
# METTI FINESTRA DAVANTI A TUTTE
TOPMOST = False
# METTI LA FINESTRA 
ZOOMED = False

###################################################################################################

root = Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
X = int(screen_width/2 - WIDTH / 2)
Y = int(screen_height/2 - HEIGHT / 2)

root.title(f"{WINDOW_TITLE}")
root.geometry(f"{WIDTH}x{HEIGHT}+{X}+{Y}")

imgicon = PhotoImage(file=f"{ICON_PATH}")
root.tk.call('wm', 'iconphoto', root._w, imgicon)

root.resizable(True,True) # (x,y)
root.minsize(MIN_SIZE_X,MIN_SIZE_Y)
root.maxsize(MAX_SIZE_X,MAX_SIZE_Y)

root.attributes("-alpha", ALPHA)
root.attributes("-fullscreen", FULLSCREEN)
root.attributes("-topmost", TOPMOST)
root.attributes("-zoomed", ZOOMED)

#root.lower()
root.lift()

root.mainloop()