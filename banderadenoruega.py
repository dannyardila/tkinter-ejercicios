# se importa la libreria tkinter con todas sus funciones 

from calendar import c
from logging import root
from tkinter import *

#----------
#ventana principal
#--------------

#se declara una variable llamada ventana principal y que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

#titulo de la ventana 
ventana_principal.title("Noruega ")

# Establecer tamaño a la ventana
ventana_principal.geometry("800x500")

#Icono de la ventana principal


#Desahabilitar boton de maximizar
ventana_principal.resizable(0,0)

#color de fondo de la pantalla principal
ventana_principal.config(bg="red")

#frame entrada
#-------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="red", width=780, height=480)
frame_entrada.place(x=10, y=10)

frame_jo = Frame(ventana_principal)
frame_jo.config(bg="blue", width=780, height=80)
frame_jo.place(x=0,  y=200)

frame_t= Frame(ventana_principal)
frame_t.config(bg="blue", width=80, height=480)
frame_t.place(x=230,  y=0)











#Se ejecuta el metodo mainloop() de la clase Tk() a traves de la instancia ventana principal.
#Este metodo despliega una ventana simple en la pantalla y queda a la espera de lo que el
#usuario haga, por ejemplo, click en boton, escribir en caja de texto, etc.
#cada accion del usuariose conoce como un evento.El metodo mainloop es un bucle infinito.










ventana_principal.mainloop()

