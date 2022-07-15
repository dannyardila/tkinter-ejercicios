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
ventana_principal.title("Danny Ferney caucho menor ")

# Establecer tamaño a la ventana
ventana_principal.geometry("800x300")

#Icono de la ventana principal


#Desahabilitar boton de maximizar
ventana_principal.resizable(0,0)

#color de fondo de la pantalla principal
ventana_principal.config(bg="red3")

#Agregar un widget a la ventana principal
letrero = Label(text="\n\nUna chimba sistemas!!\n\n",  bg="red3") 
letrero.pack()

#Agregar un widget a la ventana principal
letrero2 = Label(text="\n\nDannycito!!\n\n" , bg="red3") 
letrero2.pack()

#Agregar un widget a la ventana principal
letrero3 = Label(text="\n\n ¡Colegio san jose de guanenta¡ \n\n" , bg="red3") 
letrero3.pack()






#Se ejecuta el metodo mainloop() de la clase Tk() a traves de la instancia ventana principal.
#Este metodo despliega una ventana simple en la pantalla y queda a la espera de lo que el
#usuario haga, por ejemplo, click en boton, escribir en caja de texto, etc.
#cada accion del usuariose conoce como un evento.El metodo mainloop es un bucle infinito.










ventana_principal.mainloop()

