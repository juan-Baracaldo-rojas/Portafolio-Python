# el código tendrá que hacer lo siguiente:
# Utilice el módulo pyperclip para copiar y pegar cadenas.
# Cree dos expresiones regulares, una para números de teléfono coincidentes y otra para
# direcciones de correo electrónico coincidentes.
# Encuentra todas las coincidencias, no solo la primera coincidencia, 
# de ambas expresiones regulares.
# Formatee ordenadamente las cadenas coincidentes en una sola cadena para pegar.
# Mostrar algún tipo de mensaje si no se encontraron coincidencias en el texto.

import pyperclip
import re

# Expresiones regulares
phoneRegex = re.compile(r'''(
 (\d{3}|\(\d{3}\))? # area code
 (\s|-|\.)? # separator
 (\d{3}) # first 3 digits
 (\s|-|\.) # separator
 (\d{4}) # last 4 digits
 (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
 )''', re.VERBOSE)

#Create url regex
urlRegex=re.compile(r'(https:\/\/|http:\/\/)(\w*)(\.\w*)(.com|.es)')
mo=urlRegex.findall("http://www.youtube.com  https://www.google.com")
vec=[]
for item in mo:
    text=""
    for content in item:
        text+=str(content)
    vec.append(text)


# Create email regex.
emailRegex = re.compile(r'''(
 [a-zA-Z0-9._%+-]+ # username
 @ # @ symbol
 [a-zA-Z0-9.-]+ # domain name
 (\.[a-zA-Z]{2,4}) # dot-something
 )''', re.VERBOSE)

#Create formater Date.
dateRegex= re.compile("(((\d\d?)(\/|-|_)(\d\d?)(/|-|_)(\d\d\d\d))|((\d\d\d\d)(/|-|_)(\d\d?)(/|-|_)(\d\d?))|((\d\d)(/|-|_)(\d\d\d\d)(/|-|_)(\d\d?)))")      

# regex number card regex
numberCardRegex=re.compile(r'N° cuenta \w+')

# Find matches in clipboard text.
text = str(pyperclip.paste())

# formater unique
def formaterUnique(lista):
    vec=[]
    
    for item in lista:
        if "/" in str(item):
            text1=asigningTime(str(item).split("/"))
            vec.append(text1)
        if "-" in str(item):
            text1=asigningTime(str(item).split("-"))
            vec.append(text1)
    return vec
                
#asigning Time
def asigningTime(lista):
    year=0
    month=0
    day=0
    for index,value in enumerate(lista):
        if int(value) > 31:
            year=value
        if  int(value) >12 and int(value)<=31:
            day=value
        if int(value)<=12:
            if day==0 or month==0:
                if day ==0 :
                    day=int(value)
                if month ==0:
                    month=int(value)
                
                            
              
    return "{}/{}/{}".format(day,month,year) 

matches = []
dates=[]
for groups in dateRegex.findall(text):
    dates.append(groups[0])
for groups in formaterUnique(dates):
    matches.append(groups)
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
for groups in urlRegex.findall(text):
    text=""
    for content in groups:
        text+=str(content)
    matches.append(text)
    

# Copy results to the clipboard.
if len(matches) > 0:
 pyperclip.copy('\n'.join(matches))
 print('Copied to clipboard:')
 print('\n'.join(matches))
else:
 print('No phone numbers or email addresses found.')

