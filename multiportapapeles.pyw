# Tarea: completar muchos formularios en una página web o software con varios campos de texto.
# Si tiene varios fragmentos de texto diferentes que necesita copiar y
# pegar, tienes que seguir resaltando y copiando las mismas cosas sobre y otra vez
# Objetivo: escribir un programa en Python para realizar un seguimiento de varios fragmentos 
# de texto.
# Nota: La extensión .pyw significa que Python no se mostrarán una ventana de terminal cuando ejecuta este programa. 

# Esto es lo que hace el programa:
# Se comprueba el argumento de la línea de comandos para la palabra clave.
# • Si el argumento es guardar, el contenido del portapapeles se guarda en la palabra clave.
# • Si el argumento es una lista, todas las palabras clave se copian en el portapapeles.
# • De lo contrario, el texto de la palabra clave se copia en el teclado.
# Esto significa que el código deberá hacer lo siguiente:
# • Leer los argumentos de la línea de comandos de sys.argv.
# • Leer y escribir en el portapapeles.
# • Guardar y cargar en un archivo de estantería.

import shelve,pyperclip, sys

mcbShelf=shelve.open('mcb')
print(sys.argv, len(sys.argv), "\nsys.arg[1] ", sys.argv[1] )
if len(sys.argv) ==3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) ==3 and sys.argv[1].lower() == 'add':
    print(pyperclip.paste()[len(pyperclip.paste())-1])
    if pyperclip.paste()[len(pyperclip.paste())-1] == " ":
        print(len(pyperclip.paste()))
        mcbShelf[sys.argv[2]]+= pyperclip.paste()   
    else:
        print(len(pyperclip.paste()))
        mcbShelf[sys.argv[2]]+= " "+ pyperclip.paste() 
elif len(sys.argv) ==3 and sys.argv[1].lower() == 'addNewLine':
        mcbShelf[sys.argv[2]]+= "\n"+ pyperclip.paste()        
elif len(sys.argv) == 2:
    print("entro en el 2")
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        
        
      
        
 