from tkinter import *
import random
class ventana_principal:
    def __init__(self,master):
        self.master = master
        self.bg = Label(self.master, width = 1366, height = 720, bg ="#3498db")
        self.bg.place(x = 0, y = 0)
        self.master.attributes("-fullscreen",True)
        self.matriz_batalla = []
        self.matriz_botones = []        
        self.personajes_j1 = []
        self.personajes_j2 = []


    def menu(self):
        self.bg.lift()
        self.salir = Button(self.master, text = "Salir", command = lambda: self.master.destroy()).place(x = 1200, y = 600)
        self.jugar = Button(self.master, text = "jugar", command = lambda: self.elegir_escenario()) 
        self.jugar.place(x = 1200, y = 200)

    def elegir_escenario(self):
        self.bg.lift()
        atras = Button(self.master, text = "atras",command = lambda: self.menu()).place(x = 0, y = 0)
        self.personajes_j1 = []
        self.personajes_j2 = []
        
        self.escenario_1 = Button(self.master, text = "Escenario 1", bg ="#95a5a6" , height = 25, width = 60, command = lambda: self.crear_personaje(1))
        self.escenario_1.place(x = 20 , y = 170)
        
        self.escenario_2 = Button(self.master, text = "Escenario 2", bg ="#95a5a6" , height = 25, width = 60, command = lambda: self.crear_personaje(2))
        self.escenario_2.place(x = 460, y = 170)   

        self.escenario_3 =Button(self.master, text = "Escenario 2", bg ="#95a5a6" , height = 25, width = 60, command = lambda: self.crear_personaje(3))
        self.escenario_3.place(x = 900, y = 170)

    def crear_personaje(self,numero_escenario):
        self.bg.lift()
        self.atras = Button(self.master, text = "atras",command = lambda: self.elegir_escenario()).place(x = 0, y = 0)
        self.separador = Label(self.master, bg ="gray",height = 100).place(x = 683, y = 0)
        if self.personajes_j1 != [] or self.personajes_j2 != [] :
            self.personajes_j1 = []
            self.personajes_j2 = []
            
        if numero_escenario  == 1:
            self.daño_img_j1 = PhotoImage(file = "Recursos\Personajes\daño_1.png")
            self.defenza_img_j1 = PhotoImage(file = "Recursos\Personajes\defenza_1.png")
            self.soporte_img_j1 = PhotoImage(file = "Recursos\Personajes\soporte_1.png")

            self.daño_img_j2 = PhotoImage(file = "Recursos\Personajes\daño_1.png")
            self.defenza_img_j2 = PhotoImage(file = "Recursos\Personajes\defenza_1.png")
            self.soporte_img_j2 = PhotoImage(file = "Recursos\Personajes\soporte_1.png")
            
        elif numero_escenario == 2:
            #Cambiar nombre del archivo
            self.daño_img_j1 = PhotoImage(file = "Recursos\Personajes\daño_1.png")
            self.defenza_img_j1 = PhotoImage(file = "Recursos\Personajes\defenza_1.png")
            self.soporte_img_j1 = PhotoImage(file = "Recursos\Personajes\soporte_1.png")
            
            self.daño_img_j2 = PhotoImage(file = "Recursos\Personajes\daño_1.png")
            self.defenza_img_j2 = PhotoImage(file = "Recursos\Personajes\defenza_1.png")
            self.soporte_img_j2 = PhotoImage(file = "Recursos\Personajes\soporte_1.png")            
            
        else:
            #Cambiar nombre del archivo
            self.daño_img_j1 = PhotoImage(file = "Recursos\Personajes\daño_1.png")
            self.defenza_img_j1 = PhotoImage(file = "Recursos\Personajes\defenza_1.png")
            self.soporte_img_j1 = PhotoImage(file = "Recursos\Personajes\soporte_1.png")

            self.daño_img_j2 = PhotoImage(file = "Recursos\Personajes\daño_1.png")
            self.defenza_img_j2 = PhotoImage(file = "Recursos\Personajes\defenza_1.png")
            self.soporte_img_j2 = PhotoImage(file = "Recursos\Personajes\soporte_1.png")          

        self.daño_stats = [6,3,5,4]
        self.defenza_stats = [5,2,7,4]
        self.soporte_stats = [4,6,4,4]
        
        # Crear personaje jugador 1
        jugador_1 = Label(self.master, text = "Jugador 1").place(x = 100, y = 50)
        self.skill_points_j1 = 1000
        self.label_skill_j1 = Label(self.master, text ="Skill points: " + str(self.skill_points_j1))
        self.label_skill_j1.place(x = 200, y = 50)

        #Personajes J1
        self.daño = Button(self.master, image = self.daño_img_j1, command = lambda: self.añadir_personaje(numero_escenario,"daño","j1",self.daño_stats))
        self.daño.place(x = 100, y = 150)
        self.defenza = Button(self.master, image = self.defenza_img_j1, command = lambda: self.añadir_personaje(numero_escenario,"defenza","j1",self.defenza_stats))
        self.defenza.place(x = 200, y = 150 )
        self.soporte = Button(self.master,image = self.soporte_img_j1, command = lambda: self.añadir_personaje(numero_escenario,"soporte","j1",self.soporte_stats))
        self.soporte.place(x = 300, y = 150)
        
        # Crear personaje jugador 2
        jugador_2 = Label(self.master, text = "Jugador 2").place(x = 1200, y = 50)
        self.skill_points_j2 = 1000
        self.label_skill_j2 = Label(self.master, text ="Skill points: " + str(self.skill_points_j2))
        self.label_skill_j2.place(x = 1070, y = 50)

        #Personajes J2
        self.daño = Button(self.master, image = self.daño_img_j1, command = lambda: self.añadir_personaje(numero_escenario,"daño","j2",self.daño_stats))
        self.daño.place(x = 1200, y = 150)
        self.defenza = Button(self.master, image = self.defenza_img_j1, command = lambda: self.añadir_personaje(numero_escenario,"defenza","j2",self.defenza_stats))
        self.defenza.place(x = 1100, y = 150 )
        self.soporte = Button(self.master,image = self.soporte_img_j1, command = lambda: self.añadir_personaje(numero_escenario,"soporte","j2",self.soporte_stats))
        self.soporte.place(x = 1000, y = 150)


        #Tumbnails        
        self.x_j1 = 20
        self.y_j1 = 400

        self.x_j2 = 740
        self.y_j2 = 400

        self.lista_tumbnails_j1 = []
        self.lista_tumbnails_j2 = []


        self.iniciar = Button(self.master, text = "Iniciar Juego", state = DISABLED, command = lambda: self.iniciar_juego(numero_escenario))
        self.iniciar.place(x = 1200, y = 700)


        


    def añadir_personaje(self,escenario,tipo,jugador,max_stats):            
        if jugador == "j1":
            if self.skill_points_j1 != 0:
                self.personajes_j1 += [[tipo,self.crear_stats(max_stats)]]
                self.skill_points_j1 -= 100
                self.label_skill_j1["text"] = "Skill points: "+ str(self.skill_points_j1)
                self.crear_tumbnails(tipo,jugador)
            else:
                print("El jugador 1 no puede crear más personajes")
                
        else:
            if self.skill_points_j2 != 0:
                self.personajes_j2 += [[tipo,self.crear_stats(max_stats)]]
                self.skill_points_j2 -= 100
                self.label_skill_j2["text"] = "Skill points: "+ str(self.skill_points_j2)
                self.crear_tumbnails(tipo,jugador)
            else:
                print("El jugador 2 no puede crear más personajes")

    def crear_tumbnails(self,tipo,jugador):
        pos_matriz = len(eval("self.personajes_"+str(jugador)))
        tumbnail =  eval("self."+str(tipo)+"_img_"+jugador)
        
        if self.skill_points_j1 == 0  and self.skill_points_j2 == 0:
            self.iniciar["state"] = "normal"
        
        if jugador == "j1":
            if self.espacio_vacio(jugador):
                len_lista = len(self.lista_tumbnails_j1)
                self.x = 20
                self.y = 400
                for i in range(0,len_lista):
                    if self.lista_tumbnails_j1[i] == []:
                        self.tumbnail = Button(self.master,image = tumbnail,command = lambda: self.eliminar_tumbnail(i,jugador)) 
                        self.tumbnail.place(x = self.x, y = self.y)
                        self.lista_tumbnails_j1[i] = self.tumbnail                      
                    if self.x < 580:
                        self.x +=  70
                    else:
                        self.x = 20
                        self.y += 80
                        
            else:
                pos_lista = len(self.personajes_j1)-1
                self.tumbnail = Button(self.master,image = tumbnail,command = lambda: self.eliminar_tumbnail(pos_lista,jugador)) 
                self.tumbnail.place(x = self.x_j1, y = self.y_j1)
                self.lista_tumbnails_j1 += [self.tumbnail]
                if self.x_j1 < 580:
                    self.x_j1 +=  70
                else:
                    self.x_j1 = 20
                    self.y_j1 += 80
        else:
            if self.espacio_vacio(jugador):
                len_lista = len(self.lista_tumbnails_j2)
                self.x = 740
                self.y = 400
                for i in range(0,len_lista):
                    if self.lista_tumbnails_j2[i] == []:
                        self.tumbnail = Button(self.master,image = tumbnail,command = lambda: self.eliminar_tumbnail(i,jugador)) 
                        self.tumbnail.place(x = self.x, y = self.y)
                        self.lista_tumbnails_j2[i] = self.tumbnail                      
                    if self.x < 1260:
                        self.x +=  70
                    else:
                        self.x = 740
                        self.y += 80
            else:
                pos_lista = len(self.personajes_j2)-1
                self.tumbnail = Button(self.master,image = tumbnail,command = lambda: self.eliminar_tumbnail(pos_lista,jugador)) 
                self.tumbnail.place(x = self.x_j2, y = self.y_j2)
                self.lista_tumbnails_j2 += [self.tumbnail]
                
                if self.x_j2 < 1260:
                    self.x_j2 +=  70
                else:
                    self.x_j2 = 740
                    self.y_j2 += 80

    def espacio_vacio(self,jugador):
        if jugador == "j1":
            for i in self.lista_tumbnails_j1:
                if i == []:
                    return True
            return False
        else:
            for i in self.lista_tumbnails_j2:
                if i == []:
                    return True
            return False            
            
    def eliminar_tumbnail(self,pos,jugador):
        if jugador == "j1":
            self.lista_tumbnails_j1[pos].destroy()
            self.lista_tumbnails_j1[pos] = []
            self.personajes_j1.pop(pos)
            self.skill_points_j1 += 100
            self.label_skill_j1["text"] = "skill points: "+str(self.skill_points_j1)
            if self.skill_points_j1 != 0 or self.skill_points_j2 != 0:
                self.iniciar["state"] = "disabled"
            

        else:
            self.lista_tumbnails_j2[pos].destroy()
            self.lista_tumbnails_j2[pos] = []
            self.personajes_j2.pop(pos)
            self.skill_points_j2 += 100
            self.label_skill_j2["text"] = "skill points: "+str(self.skill_points_j2)
            if self.skill_points_j1 != 0 or self.skill_points_j2 != 0:
                self.iniciar["state"] = "disabled"
            
            
    def crear_stats(self,max_stats):
        stats = []
        for i in max_stats:
            stats += [random.randint(1,i)]  
        return stats
    
    def iniciar_juego(self,escenario):
        self.bg.lift()
        self.tablero()
        self.tumbnails_jugadores()
        self.stats()
        self.matriz_vacia()
        self.botones_tablero ()
        
        
    def tablero (self):
        #print(self.personajes_j1)
        self.label_j1 = Label(self.master,text = "Jugador 1",font = ("Arial",25)).place(x= 0, y = 0)
        self.label_j2 = Label(self.master,text = "Jugador 2",font = ("Arial",25)).place(x= 1220, y = 0)
        
        self.matriz_vacia()
        self.botones_tablero()
        self.tumbnails_jugadores()
        self.stats()

    def tumbnails_jugadores(self):

        for i in range(10):
            url ="Recursos\Interfaz\\"+str(self.personajes_j1[i][0])+".png"
            print(url)            
            imagen = PhotoImage(file = "Recursos\Interfaz\\"+str(self.personajes_j1[i][0])+".png")
            boton = Button(self.master,image = imagen)
            boton.place(x = 0, y = 20)
            
    #def mostrar_stats(self):
        
        
    def stats(self):
        self.menu_stats_j1 = Label(self.master, height = 35, width = 35)
        self.menu_stats_j1.place(x = 0, y = 170)
        self.menu_stats_j2 = Label(self.master, height = 35, width = 35)
        self.menu_stats_j2.place(x = 1120, y = 170)
        
    def botones_tablero (self):
        self.soporte_img_j1 = PhotoImage(file = "Recursos\Personajes\soporte_1.png")
        self.vector_botones = []
        x = 380
        y = 100
        for i in range(7):
            for j in range(6):
                boton = Button(self.master,image = self.soporte_img_j1,height = 6,width = 11)
                boton.place(x = x, y = y)
                if x < 896:
                   x +=  86
                else:
                    x = 380
                    y += 100              
                self.vector_botones += [boton]
            self.matriz_botones += [self.vector_botones]
            self.vector_botones = []
  
            
    def matriz_vacia(self):
        self.vector = []
        for i in range(6):
            for j in range(7):
                self.vector += [0]
            self.matriz_batalla += [self.vector]
            self.vector = []
    

root = Tk()
aplicacion = ventana_principal(root)
#aplicacion.iniciar_juego(1)
aplicacion.crear_personaje(1)
root.mainloop()
