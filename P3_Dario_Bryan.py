from tkinter import *

class ventana_principal:
    def __init__(self,master):
        self.master = master
        master.attributes("-fullscreen",True)
        self.boton = Button(self.master, text = "Salir", command = lambda: self.master.destroy()).place(x=0,y=0)


root = Tk()
aplicacion = ventana_principal(root)
root.mainloop()
