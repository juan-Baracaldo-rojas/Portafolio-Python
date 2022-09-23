# output: linea a linea del texto
def openWithFor():
    print("ingreso a openWithFor()")
    data=open("example1.txt")
    contador=0
    for line in data:
        print(line)
        contador+=1
    print('Contador: %i'.center(3," ") %contador)
openWithFor()

# output: caracter a caracter del texto
def openwithRead():
    print("ingreso a openwithRead()")
    data=open("example1.txt")
    inputD=data.read()
    print(len(inputD))
    print(inputD)
openwithRead()
 