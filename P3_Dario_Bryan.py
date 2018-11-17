from tkinter import *
from PIL import Image, ImageTk
class ventana_principal:
    def __init__(self,master):
        self.master = master
        self.bg = Label(self.master, width = 1366, height = 720, bg ="#3498db")
        self.bg.place(x = 0, y = 0)
        self.master.attributes("-fullscreen",True)        
        self.menu()

    def menu(self):
        self.bg.lift()
        self.salir = Button(self.master, text = "Salir", command = lambda: self.master.destroy()).place(x = 1200, y = 600)
        self.jugar = Button(self.master, text = "jugar", command = lambda: self.elegir_escenario()) 
        self.jugar.place(x = 1200, y = 200)

    def elegir_escenario(self):
        self.bg.lift()
        atras = Button(self.master, text = "atras",command = lambda: self.menu()).place(x = 0, y = 0)

        self.escenario_1 = Button(self.master, text = "Escenario 1", bg ="#95a5a6" , height = 25, width = 60, command = lambda: self.crear_personaje(1))
        self.escenario_1.place(x = 20 , y = 170)
        
        self.escenario_2 = Button(self.master, text = "Escenario 2", bg ="#95a5a6" , height = 25, width = 60, command = lambda: self.crear_personaje(2))
        self.escenario_2.place(x = 460, y = 170)   

        self.escenario_3 =Button(self.master, text = "Escenario 2", bg ="#95a5a6" , height = 25, width = 60, command = lambda: self.crear_personaje(3))
        self.escenario_3.place(x = 900, y = 170)
        
    def crear_personaje(self,numero_escenario):
        self.bg.lift()
        atras = Button(self.master, text = "atras",command = lambda: self.elegir_escenario()).place(x = 0, y = 0)
        jugador_1 = Label(self.master, text = "Jugador 1").place(x = 100, y = 50)
        self.skill_point = 0
        label_skill = Label(self.master, text = self.skill_point)
        label_skill.place(x = 150, y = 50)
        boton = Button(self.master, text = "cambiar", command = lambda:self.sumar())
        boton.place(x = 200, y = 350)

    def sumar(self):
        self.skill_point+=1
        print(self.skill_point)
        
        
        
        
        
        
        
                            


root = Tk()
aplicacion = ventana_principal(root)
root.mainloop()
