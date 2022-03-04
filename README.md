# Gestionar-Archivos-Python
Sencillo Script que nos permite comprimir una carpeta con los archivos que queramos y enviarla a una determinada ubicación. Ideal para automatizar la compresión de copias de seguridad y enviarlas a la ubicación que queramos.

Se incluyen las instrucciones para configurar el script dentro de la interfaz del mismo programa.

--------------------------------------------------------------------------------------------------------------

EXPLICACIÓN DEL CÓDIGO:

Este script fue programado en Python utilizando los módulos OS, shutil, tkinter y zipfile. En primer lugar, he creado la interfaz gráfica con Tkinter quye incluye el botón de comprimir y un pequeño texto con las instrucciones de configuración. Por otra parte, dentro del botón para comprimir se incluye una función que es la que ejecuta el resto del código donde se comprime el archivo gracias al módulo zipfile y después de mueve a otro directorio a través del módulo shutil. 

