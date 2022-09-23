# * Busca todos los nombres de archivo en el directorio de trabajo actual para
#   fechas al estilo americano.
# * Cuando se encuentra uno, cambia el nombre  del archivo con el mes y el día 
#   intercambiados para hacerlo al estilo   europeo. Esto significa que el código 
#   deberá hacer lo siguiente:
# * Cree una expresión regular que pueda identificar el patrón de texto de las 
#   fechas de estilo estadounidense.
# * Llame a os.listdir() para buscar todos los archivos en el directorio de trabajo.
# * Recorra cada nombre de archivo, usando la expresión 
#   regular para verificar si tiene una fecha.
# • Si tiene una fecha, cambie el nombre del archivo 
#   con shutil.move().
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.
from fileinput import filename
import re, os, shutil
dateRegex=re.compile(r'''(.*?)
                     ((0|1)?\d)-
                     ((0|1|2|3)?\d)-
                     ((19|20)\d\d)
                     (.*?)$
                     ''',re.VERBOSE)
# TODO: Loop over the files in the working directory.
path='C:\\Users\\Juan\\Documents\\respaldo pc juanma\\Python\\DESARROLLO_FINES_DE_SEMANA\\automate_boring_thimgs_with_python\\10_08_2022'
for amerFilename in os.listdir(path):
    print("amerFilename: ",amerFilename)
    mo = dateRegex.search(amerFilename)
    print("mo: ",mo,"\n")
# TODO: Skip files without a date.
    if mo == None:
        continue
    
    # mo=dateRegex.findall(filename)[0]
    beforePart = mo.group(1)
    print("beforePart : ",beforePart)
    monthPart = mo.group(2)
    print("monthPart : ",monthPart)
    dayPart = mo.group(4)
    print("dayPart : ",dayPart)
    yearPart = mo.group(6)
    print("yearPart : ",yearPart)
    afterPart = mo.group(8)
    print("afterPart : ",afterPart)
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    print("amerFilename: ",amerFilename,"\n")
    print("euroFilename: ",euroFilename,"\n")
    
     # Rename the files.
    #  Nota
    # primero pruebe con prints y luego descomente el shuntil
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
   
    # shutil.move(amerFilename, euroFilename)
# TODO  FALTA PROVAR EL PROGRAMA

