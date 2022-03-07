import os
import shutil
import re
from tkinter import messagebox as MessageBox
from tkinter import *

def getTextInput():
    result=escribirrutas.get()
    print("El usuario para la ruta es",result)
    patron = r"\s+"
    resultado = re.sub(patron, "", result)
    print(resultado)
    definirrutas(resultado)
    
def definirrutas(resultado):
    rutaorigen = "/Users/{}/Desktop/carpetaorigen/".format(resultado)
    rutadestino = "/Users/{}/Desktop/carpetadestino/".format(resultado)
    accion(rutaorigen, rutadestino, resultado)

def accion(rutaorigen, rutadestino, resultado):
    os.chdir("/Users/{}/Desktop/carpetaorigen/".format(resultado))
    shutil.make_archive("carpeta_comprimida","zip", "carpeta_añadir_archivos_comprimir")
    shutil.move(rutaorigen + "carpeta_comprimida.zip", rutadestino)

def popup():
    MessageBox.showinfo("Sobre mí","Enlace a mi perfil de LinkedIn:\nhttps://www.linkedin.com/in/maalfer1/")
    

root = Tk()
root.config(bd=15)
root.title("Script para automatizar la compresión y envío de archivos") 
menubar = Menu(root) # Creamos el menú.
root.config(menu=menubar)

helpmenu = Menu(menubar, tearoff=0) # Modificamos el menú de ayuda.
helpmenu.add_command(label="Información del autor",command=popup)

menubar.add_cascade(label="Para más información", menu=helpmenu)
menubar.add_separator()
menubar.add_command(label="Salir", command=root.destroy)


instrucciones = Label(root, text="Con este sencillo script podremos comprimir los archivos de un directorio y enviarlos a otra ubicación.\n.\nPaso nº1 - Crear dos carpetas en el escritorio, una será carpetaorigen y la otra carpetadestino\nPaso nº2 - Dentro de carpetaorigen crear una carpeta llamada carpeta_añadir_archivos_comprimir, donde contendrá los archivos que queramos mover.\n Paso nº3 - Modificar, si es necesario, las rutas de las dos carpetas y poner otras direcciones.\n Paso 4º- Escribir el nombre de usuario de tu ordenador\n\n")
instrucciones.grid(row=0, column=1)


escribirrutas = Entry(root)
escribirrutas.grid(row=2, column=1)

boton = Button(root, text="Clícame para comprimir y mover el archivo <3", command=getTextInput)
boton.grid(row=3, column=1)

root.mainloop()
