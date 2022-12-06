test=['\n Roma, Bogotá\n    ', '\n\n        57 ㎡\n      ', '\n\n        Piso \n', '\n\n        3\n      ', 'no incluye', '\n\n        1\n      ', '\n      $11 millones\n      ']

def limpiarDatos():
    # datosLimpios=[]
    # for casa in lista:
        # vec=[]
        print(test[0].split("\n")[1])
        if "\n" in test[1]:
            print(float(test[1].split("\n")[2].strip().split(" ")[0]))
        if "\n" not in test[1]:
            print(float(test[1]))
        
        print(test[2].strip())
        print(int(test[3].split("\n")[2].strip()))
        if test[4] != "no incluye":
            print(test[4].split("\n")[1].split("Incluye:")[1].split("·"))
        print(int(test[5].split("\n")[2].strip()))
        if "\n" in test[6]:
            print(int(test[6].split("\n")[1].strip().split(" ")[0].split("$")[1]))    
        if "\n" not in test[6]:
            print(int(test[6].split(" ")[0][1:]))
        # datosLimpios.append(vec)
    # return datosLimpios
    
    
limpiarDatos()






