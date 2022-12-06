import sys
class analysedText(object):
    
    #Constructor
    # formatedText: Asigna el formato del texto a analizar
    def __init__ (self, text):
        #   quita lps .!?,
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        # comvierte el textyo en minusculas
        formattedText = formattedText.lower()
        ##fmt lee la entrada de los argumentosdel archivo en la línea de comando; cuando no hay ninguno de estos, lee desde la entrada estándar.
        self.fmtText = formattedText
 
    # Metodo: freqAll()  -
    # descripcion: metodo que cuenta las veces qe se repite una palabra y asu vez las guarda en un 
    #              diccionario el cual retorna
    # wordList: Lista que contiene las palabras del texto
    # freqMap: Diccionario que contiene la palabra junto con numero de veces repetidas dentro de la pabra
    # retorna : freqmap
    def freqAll(self):        
        # Separa las palabras del texto en una lista
        wordList = self.fmtText.split(' ')
        
        # Crea diciionario
        freqMap = {}
        for word in set(wordList): # usamos set para quitar los datos iguales
            freqMap[word] = wordList.count(word)
        
        return freqMap
    # metodo: freqOf(word)  
    # descripcion: muestra el rating de el parametro word  
    # parametros: 
    #     word: palabra a la cual se le quiere oetene la frecuencia    
    def freqOf(self,word):
        # obtener mapa de frecuencia
        freqDict = self.freqAll()
        #mira si la palabra esta en el diccionario de frecuencias
        if word in freqDict:
            return freqDict[word]
        else:
            return 0

# sampleMap====Mapa de muestra
sampleMap = {'eirmod': 1,'sed': 1, 'amet': 2, 'diam': 5, 'consetetur': 1, 'labore': 1, 'tempor': 1, 'dolor': 1, 'magna': 2, 'et': 3, 'nonumy': 1, 'ipsum': 1, 'lorem': 2}

#Funcion metodo testMsg
#metodo para arrojar un mensaje segun el bolenao que le llega como parametro
def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return 'Test Failed'

print("Constructor: ")
#significado variables
#sample passage === hace referecia a una muestra  la cual es el parametro que manda atravez de la clase analisedText
#
# analisedText == es la clase creada para generar 8na analisis de los texo
# sample.fmtText=obtiene el formato original del texto y lo comopara con la cadena que esta a la desrecha                   
try:
    samplePassage = analysedText("Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")
    print(testMsg(samplePassage.fmtText == "lorem ipsum dolor diam amet consetetur lorem magna sed diam nonumy eirmod tempor diam et labore et diam magna et diam amet"))
except:
#Si encuentra un error arroja el siguiente mensaje    
    print("Error detected. Recheck your function " )
print("freqAll: ")
#Esta exepcion se ultiliza para obtener un diccionario al llamar al metodo freqAll()
#testea el mensaje mediante el metodo testMsg el cul manda como parametro la comparacion entre el diccionario de frecuencias y
#lo compara con la muestra que es sampleMap

try:
    wordMap = samplePassage.freqAll()
    print(testMsg(wordMap==sampleMap))
except:
    print("Error detected. Recheck your function " )
print("freqOf: ")
##esta escepcion se usa para validar si las palabras que se encuentran en la muestra de palabras y  mira si es diferentel
#a la cadena que retorna el metodo freqOf
try:
    passed = True
    for word in sampleMap:
        if samplePassage.freqOf(word) != sampleMap[word]:
            #Si el valor no esta en el diccionario arroja falso  
            passed = False
            #Rompe el ciclo for
            break
    #Manda como parametro el booleano passed atraves del validador    
    print(testMsg(passed))
    
except:
    print("Error detected. Recheck your function  " )

   