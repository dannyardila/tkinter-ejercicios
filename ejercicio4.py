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
ventana_principal.title("Nigeria")

# Establecer tamaño a la ventana
ventana_principal.geometry("800x500")

#Icono de la ventana principal


#Desahabilitar boton de maximizar
ventana_principal.resizable(0,0)

#color de fondo de la pantalla principal
ventana_principal.config(bg="white")

#---------
#frame entrada
#-------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="green", width=270, height=480)
frame_entrada.place(x=10, y=10)

#frame operaciones
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=500, height=480)
frame_operaciones.place(x=270, y=10)

#frame resultado
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="green", width=270, height=480)
frame_resultados.place(x=530, y=10)













#Se ejecuta el metodo mainloop() de la clase Tk() a traves de la instancia ventana principal.
#Este metodo despliega una ventana simple en la pantalla y queda a la espera de lo que el
#usuario haga, por ejemplo, click en boton, escribir en caja de texto, etc.
#cada accion del usuariose conoce como un evento.El metodo mainloop es un bucle infinito.










ventana_principal.mainloop()

