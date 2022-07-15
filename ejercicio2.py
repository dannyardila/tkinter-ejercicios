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
ventana_principal.title("Paises bajos ")

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
frame_entrada.config(bg="red", width=780, height=240)
frame_entrada.place(x=10, y=10)

#frame operaciones
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=780, height=300)
frame_operaciones.place(x=10, y=250)

#frame resultado
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="blue", width=780, height=160)
frame_resultados.place(x=10, y=330)













#Se ejecuta el metodo mainloop() de la clase Tk() a traves de la instancia ventana principal.
#Este metodo despliega una ventana simple en la pantalla y queda a la espera de lo que el
#usuario haga, por ejemplo, click en boton, escribir en caja de texto, etc.
#cada accion del usuariose conoce como un evento.El metodo mainloop es un bucle infinito.










ventana_principal.mainloop()

