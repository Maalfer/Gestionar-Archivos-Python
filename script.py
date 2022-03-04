import os
import zipfile
import shutil
from tkinter import *

def accion():
    os.chdir("/Users/mario/Desktop/carpetaorigen/") # Modificar esta ruta
    rutaorigen = "/Users/mario/Desktop/carpetaorigen/" # Modificar esta ruta
    rutadestino = "/Users/mario/Desktop/carpetadestino/" # Modificar esta ruta
    archivo_zip = shutil.make_archive("carpeta_comprimida","zip", "carpeta_añadir_archivos_comprimir")
    shutil.move(rutaorigen + "carpeta_comprimida.zip", rutadestino) 


root = Tk()
root.config(bd=15)
root.title("Script para automatizar la compresión y envío de archivos") 

texto = Label(root, text="INSTRUCCIONES DE USO\n\nCon este sencillo script podremos comprimir los archivos de un directorio y enviarlos a otra ubicación.\nTan solo debes modificar el código de este programa y adaptar las rutas y nombres de los archivos que quieras automatizar.\nLos archivos que quieras automatizar deben ir dentro de la carpeta_añadir_archivos_comprimir y debe encontrarse en la misma ruta de la variable rutaorigen.\nEn cuanto a la ruta destino, también debes modificar el contenido de esa variable con la ruta que quieras enviar el archivo comprimido\n\n") # Y esto una etiqueta con la palabra texto.
texto.grid(row=1, column=1)

boton = Button(root, text="Clícame para comprimir y mover el archivo :)", command=accion)
boton.grid(row=3, column=1)


root.mainloop()