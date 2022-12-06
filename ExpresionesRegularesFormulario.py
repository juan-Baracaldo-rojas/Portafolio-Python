import re

#Expreciones Regulares
eR_nombres="[a-zA-zA-Z]{2,13}"
expresion_regular_apellidos="[a-zA-zA-Z]{2,20}"
expresion_regular_direccion="(Cr|Dg|Clj|Cl)(([ ][0-9]{1,3}\#[ ][0-9]{1,3}[ ][0-9]{1,3})|([ ][0-9]{1,2}[ ]\#[0-9]{1,3}[ ][0-9]{1,3})|([ ][0-9]{1,2}\#[0-9]{1,3}[ ][0-9]{1,3})|([ ][0-9]{1,2}[ ]\#[ ][0-9]{1,3}[ ][0-9]{1,3}))"
expresion_regular_correo="[\w._%+-]+@(uptc|gmail)[.]((edu[.][co])|com)"
expresion_regular_fecha_de_nacimiento="((^[1-2]{1}[0-9]{1}|^[1-9]{1}|^[0]{1}[1-9]{1})|[3]{1}[0]{1})+(['/']{1}[468]{1}['/']{1}|['/0']{2}[468]{1}['/']{1}|['/'][1]{1}[2]['/'])+((20[0-1]{1}[0-9]{1})|(19+[0-9]{2}))"+"|((^[1-2]{1}[0-9]{1}|^[1-9]{1}|^[0]{1}[1-9]{1})|[3]{1}[0-1]{1})+(['/']{1}[13579]{1}['/']{1}|['/0']{2}[13579]{1}['/']{1}|['/'][1]{1}[1]['/'])+((20[0-1]{1}[0-9]{1})|(19+[0-9]{2}))"+"|((^[1-2]{1}[0-9]{1})|(^[0]+[1-9]{1})|(!^[1-9]{1}))+(['/2/']|['/02/'])+((20[0-1]{1}[0-9]{1})|(19+[0-9]{2}))"
expresion_regular_celular="(\+[0-9]{2}([ |-])3(([0-9]{9})|([0-9]{2}[ ][0-9]{3}[ ][0-9]{4})|([0-9]{2}[-][0-9]{3}[-][0-9]{4})))|3([0-9]{9})"
expresion_regular_telefono_fijo="(\+[0-9]{1,2}[ ]\([0-9]{1,3}\)[ ][0-9]{7})|([1-8]{1}[0-9]{2}[ ][0-9]{2}[ ][0-9]{2})"
expresion_regular_Codigo_postal="[0-9]{6}"

print("""*************************************************************************
**************** FORMULARIO DE REGISTRO UPTC Y GMAIL ********************
************************************************************************* """)

#inputs de los datos
primer_nombre=input("Digite su primer nombre: ")
segundo_nombre=input("Digite su segundo nombre: ")
primer_apellido=input("Digite su primer apellido: ")
segundo_apellido=input("Digite su segundo apellido: ")
direccion=input("Digite su direccion: ")
correo=input("Digite su correo de la universidad o Gmail: ")
fecha=input("Digite su fecha: ")
celular=input("Digite su celular: ")
telefono_fijo=input("Digite su telefono fijo: ")
codigoPostal=input("Digite su numero de codigo postal: ")


print("******************************* RESULTADOS *******************************")


#METODOS DE VALIDACION
def validacionPrimerNombre():
    var_1nombre=re.findall(eR_nombres,primer_nombre)
    if len(var_1nombre) == 1:
        if str(var_1nombre[0]) == primer_nombre:
            print(" El primer nombre :"+ str(primer_nombre) +"                   cumple con la expresion regular")
        else:
            print(" El primer nombre :"+ str(primer_nombre) +"                    no cumple con la expresion regular")    
    else:
        print(" El primer nombre :"+ str(primer_nombre) +"                         no cumple con la expresion regular")
validacionPrimerNombre()        

def validacionSegundoNombre():
    var_2nombre=re.findall(eR_nombres,segundo_nombre)
    if len(var_2nombre) == 1:
        if str(var_2nombre[0]) == segundo_nombre:
            print(" El segundo nombre :"+ str(segundo_nombre) +"                   cumple con la expresion regular")
        else:
          print(" El segundo nombre :"+ str(segundo_nombre) +"                     no cumple con la expresion regular")
    else:
        print(" El segundo nombre :"+ str(segundo_nombre) +"                       no cumple con la expresion regular")
validacionSegundoNombre()    

def validacionPrimerApellido():
    var_1Apellido=re.findall(expresion_regular_apellidos,primer_apellido)
    if len(var_1Apellido) == 1:
        if str(var_1Apellido[0]) == primer_apellido:
            print(" El primer apellido  :"+ str(primer_apellido) +"                cumple con la expresion regular")
        else:
            print(" El primer apellido :"+ str(primer_apellido) +"                 no cumple con la expresion regular")
        
    else:
        print(" El primer apellido :"+ str(primer_apellido) +"                     no cumple con la expresion regular")
validacionPrimerApellido()        

def validacionSegundoApellido():
    var_2Apellido=re.findall(expresion_regular_apellidos,segundo_apellido)
    if len(var_2Apellido) == 1:
        if str(var_2Apellido[0]) == segundo_apellido:
            print(" eE segundo apellido :"+ str(segundo_apellido) +"                cumple con la expresion regular")
        else:
            print(" el segundo apellido :"+ str(segundo_apellido) +"                no cumple con la expresion regular")
        
    else:
        print(" el segundo apellido :"+ str(segundo_apellido) +"                    no cumple con la expresion regular")
validacionSegundoApellido()

def validacionDireccion():
    varDir=re.fullmatch(expresion_regular_direccion,direccion)
    if varDir != None:
         print(" La direccion :"+ str(direccion) +"                    cumple con la expresion regular")
    else:
        print(" La direccion :"+ str(direccion) +"                     no cumple con la expresion regular")
validacionDireccion()

def validacionCorreo():
    varCor=re.findall(expresion_regular_correo,correo)
    if len(varCor) != 0:
        print(" El correo :"+ str(correo) +"                         cumple con la expresion regular")
    else:
        print(" EL correo :"+ str(correo) +"                             no cumple con la expresion regular")
validacionCorreo()        

def validarFechaNacimiento():
    varFecNac=re.findall(expresion_regular_fecha_de_nacimiento,fecha)
    if len(varFecNac) != 0:
         print(" La fecha de nacimiento :"+ str(fecha) +"             cumple con la expresion regular")
    else:
        print(" La fecha de nacimiento :"+ str(fecha) + "                no cumple con la expresion regular")
validarFechaNacimiento()        


def validacionCelular():
    varCel=re.fullmatch(expresion_regular_celular,celular)
    if varCel != None:
       print(" El celular: "+ str(celular) +"                       cumple con la expresion regular")
    else :
       print(" El celular: "+ str(celular) +"                       no cumple con la expresion regular") 
validacionCelular()

def validacionTelefono():
    varTel=re.fullmatch(expresion_regular_telefono_fijo,telefono_fijo)
    if varTel != None:
        print(" El telefono fijo: "+ str(telefono_fijo) +"                           cumple con la expresion regular")
    else:
        print(" El telefono fijo: "+ str(telefono_fijo) +"                           no cumple con la expresion regular")
validacionTelefono()

def validarCodigoPostal():
    varCod=re.fullmatch(expresion_regular_Codigo_postal,codigoPostal)
    if varCod != None:
       print(" El telefono fijo: "+ str(codigoPostal) +"                               cumple con la expresion regular")
    else:
       print(" El telefono fijo: "+ str(codigoPostal) +"                               no cumple con la expresion regular")
validarCodigoPostal        


#codigo_postal=input("Digite su codigo postal")
