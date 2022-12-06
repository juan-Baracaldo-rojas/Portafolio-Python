
from experta import *

from tkinter import *

class Casa(Fact):
    ubicacion=Field(str)
    area=Field(float)
    precio=Field(float)
    numeroBaños=Field(int)


class SugerenciaCasa(KnowledgeEngine):


    @Rule(Casa(ubicacion="Suba, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio <316.0),
    TEST(lambda precio: precio >=336.0),
    TEST(lambda numeroBaños: numeroBaños <=3),
    TEST(lambda area: area <92.8),
    TEST(lambda area: area >=98.4))
    def pruebaPrecioSubaBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#49FF33",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una buena compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Suba, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio >=316.0),
    TEST(lambda precio: precio <336.0),
    TEST(lambda numeroBaños: numeroBaños >=3),
    TEST(lambda area: area >=92.8),
    TEST(lambda area: area <98.4))
    def pruebaPrecioSubaBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#FF4633",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una mala compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Lagos de Torca, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio <880.0),
    TEST(lambda precio: precio >=1320.0),
    TEST(lambda numeroBaños: numeroBaños <=5),
    TEST(lambda area: area <171.2),
    TEST(lambda area: area >=256.8))
    def pruebaPrecioLagosdeTorcaBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#49FF33",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una buena compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Lagos de Torca, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio >=880.0),
    TEST(lambda precio: precio <1320.0),
    TEST(lambda numeroBaños: numeroBaños >=5),
    TEST(lambda area: area >=171.2),
    TEST(lambda area: area <256.8))
    def pruebaPrecioLagosdeTorcaBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#FF4633",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una mala compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Kennedy, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio <152.0),
    TEST(lambda precio: precio >=228.0),
    TEST(lambda numeroBaños: numeroBaños <=2),
    TEST(lambda area: area <56.0),
    TEST(lambda area: area >=84.0))
    def pruebaPrecioKennedyBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#49FF33",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una buena compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Kennedy, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio >=152.0),
    TEST(lambda precio: precio <228.0),
    TEST(lambda numeroBaños: numeroBaños >=2),
    TEST(lambda area: area >=56.0),
    TEST(lambda area: area <84.0))
    def pruebaPrecioKennedyBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#FF4633",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una mala compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Usaquén, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio <4160.0),
    TEST(lambda precio: precio >=1380.0),
    TEST(lambda numeroBaños: numeroBaños <=4),
    TEST(lambda area: area <394.4),
    TEST(lambda area: area >=284.4))
    def pruebaPrecioUsaquénBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#49FF33",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una buena compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Usaquén, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio >=4160.0),
    TEST(lambda precio: precio <1380.0),
    TEST(lambda numeroBaños: numeroBaños >=4),
    TEST(lambda area: area >=394.4),
    TEST(lambda area: area <284.4))
    def pruebaPrecioUsaquénBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#FF4633",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una mala compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Cedritos, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio <1480.0),
    TEST(lambda precio: precio >=591.6),
    TEST(lambda numeroBaños: numeroBaños <=2),
    TEST(lambda area: area <240.0),
    TEST(lambda area: area >=151.2))
    def pruebaPrecioCedritosBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#49FF33",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una buena compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Cedritos, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio >=1480.0),
    TEST(lambda precio: precio <591.6),
    TEST(lambda numeroBaños: numeroBaños >=2),
    TEST(lambda area: area >=240.0),
    TEST(lambda area: area <151.2))
    def pruebaPrecioCedritosBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#FF4633",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una mala compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Verbenal, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio <440.0),
    TEST(lambda precio: precio >=312.0),
    TEST(lambda numeroBaños: numeroBaños <=2),
    TEST(lambda area: area <115.47200000000001),
    TEST(lambda area: area >=96.0))
    def pruebaPrecioVerbenalBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#49FF33",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una buena compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Verbenal, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio >=440.0),
    TEST(lambda precio: precio <312.0),
    TEST(lambda numeroBaños: numeroBaños >=2),
    TEST(lambda area: area >=115.47200000000001),
    TEST(lambda area: area <96.0))
    def pruebaPrecioVerbenalBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#FF4633",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una mala compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Patio Bonito, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio <120.0),
    TEST(lambda precio: precio >=180.0),
    TEST(lambda numeroBaños: numeroBaños <=1),
    TEST(lambda area: area <36.0),
    TEST(lambda area: area >=54.0))
    def pruebaPrecioPatioBonitoBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#49FF33",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una buena compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Patio Bonito, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio >=120.0),
    TEST(lambda precio: precio <180.0),
    TEST(lambda numeroBaños: numeroBaños >=1),
    TEST(lambda area: area >=36.0),
    TEST(lambda area: area <54.0))
    def pruebaPrecioPatioBonitoBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#FF4633",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una mala compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Chicó, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio <1360.0),
    TEST(lambda precio: precio >=2040.0),
    TEST(lambda numeroBaños: numeroBaños <=6),
    TEST(lambda area: area <237.00799999999998),
    TEST(lambda area: area >=355.512))
    def pruebaPrecioChicóBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#49FF33",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una buena compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Chicó, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio >=1360.0),
    TEST(lambda precio: precio <2040.0),
    TEST(lambda numeroBaños: numeroBaños >=6),
    TEST(lambda area: area >=237.00799999999998),
    TEST(lambda area: area <355.512))
    def pruebaPrecioChicóBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#FF4633",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una mala compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Britalia Norte, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio <632.0),
    TEST(lambda precio: precio >=312.0),
    TEST(lambda numeroBaños: numeroBaños <=2),
    TEST(lambda area: area <149.6),
    TEST(lambda area: area >=85.2))
    def pruebaPrecioBritaliaNorteBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#49FF33",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una buena compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Britalia Norte, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio >=632.0),
    TEST(lambda precio: precio <312.0),
    TEST(lambda numeroBaños: numeroBaños >=2),
    TEST(lambda area: area >=149.6),
    TEST(lambda area: area <85.2))
    def pruebaPrecioBritaliaNorteBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#FF4633",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una mala compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Colina Campestre, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio <1040.0),
    TEST(lambda precio: precio >=780.0),
    TEST(lambda numeroBaños: numeroBaños <=3),
    TEST(lambda area: area <208.0),
    TEST(lambda area: area >=194.68800000000002))
    def pruebaPrecioColinaCampestreBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#49FF33",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una buena compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Colina Campestre, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio >=1040.0),
    TEST(lambda precio: precio <780.0),
    TEST(lambda numeroBaños: numeroBaños >=3),
    TEST(lambda area: area >=208.0),
    TEST(lambda area: area <194.68800000000002))
    def pruebaPrecioColinaCampestreBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#FF4633",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una mala compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Bosa, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio <96.0),
    TEST(lambda precio: precio >=144.0),
    TEST(lambda numeroBaños: numeroBaños <=2),
    TEST(lambda area: area <16.8),
    TEST(lambda area: area >=25.2))
    def pruebaPrecioBosaBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#49FF33",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una buena compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Bosa, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio >=96.0),
    TEST(lambda precio: precio <144.0),
    TEST(lambda numeroBaños: numeroBaños >=2),
    TEST(lambda area: area >=16.8),
    TEST(lambda area: area <25.2))
    def pruebaPrecioBosaBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#FF4633",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una mala compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Engativá, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio <268.0),
    TEST(lambda precio: precio >=348.0),
    TEST(lambda numeroBaños: numeroBaños <=2),
    TEST(lambda area: area <67.52000000000001),
    TEST(lambda area: area >=0.0))
    def pruebaPrecioEngativáBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#49FF33",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una buena compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Engativá, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio >=268.0),
    TEST(lambda precio: precio <348.0),
    TEST(lambda numeroBaños: numeroBaños >=2),
    TEST(lambda area: area >=67.52000000000001),
    TEST(lambda area: area <0.0))
    def pruebaPrecioEngativáBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#FF4633",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una mala compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="El Tintal, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio <150.4),
    TEST(lambda precio: precio >=225.6),
    TEST(lambda numeroBaños: numeroBaños <=2),
    TEST(lambda area: area <54.4),
    TEST(lambda area: area >=81.6))
    def pruebaPrecioElTintalBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#49FF33",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una buena compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="El Tintal, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio >=150.4),
    TEST(lambda precio: precio <225.6),
    TEST(lambda numeroBaños: numeroBaños >=2),
    TEST(lambda area: area >=54.4),
    TEST(lambda area: area <81.6))
    def pruebaPrecioElTintalBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#FF4633",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una mala compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Toberín, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio <616.0),
    TEST(lambda precio: precio >=732.0),
    TEST(lambda numeroBaños: numeroBaños <=2),
    TEST(lambda area: area <127.2),
    TEST(lambda area: area >=178.08))
    def pruebaPrecioToberínBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#49FF33",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una buena compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Toberín, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio >=616.0),
    TEST(lambda precio: precio <732.0),
    TEST(lambda numeroBaños: numeroBaños >=2),
    TEST(lambda area: area >=127.2),
    TEST(lambda area: area <178.08))
    def pruebaPrecioToberínBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#FF4633",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una mala compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Santa Isabel, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio <576.0),
    TEST(lambda precio: precio >=864.0),
    TEST(lambda numeroBaños: numeroBaños <=3),
    TEST(lambda area: area <214.4),
    TEST(lambda area: area >=321.6))
    def pruebaPrecioSantaIsabelBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#49FF33",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una buena compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Santa Isabel, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio >=576.0),
    TEST(lambda precio: precio <864.0),
    TEST(lambda numeroBaños: numeroBaños >=3),
    TEST(lambda area: area >=214.4),
    TEST(lambda area: area <321.6))
    def pruebaPrecioSantaIsabelBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#FF4633",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una mala compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Fontibón, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio <412.0),
    TEST(lambda precio: precio >=444.0),
    TEST(lambda numeroBaños: numeroBaños <=3),
    TEST(lambda area: area <320.0),
    TEST(lambda area: area >=259.2))
    def pruebaPrecioFontibónBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#49FF33",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una buena compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Fontibón, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio >=412.0),
    TEST(lambda precio: precio <444.0),
    TEST(lambda numeroBaños: numeroBaños >=3),
    TEST(lambda area: area >=320.0),
    TEST(lambda area: area <259.2))
    def pruebaPrecioFontibónBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#FF4633",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una mala compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="La Carolina, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio <784.0),
    TEST(lambda precio: precio >=1176.0),
    TEST(lambda numeroBaños: numeroBaños <=3),
    TEST(lambda area: area <160.8),
    TEST(lambda area: area >=241.2))
    def pruebaPrecioLaCarolinaBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#49FF33",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una buena compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="La Carolina, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio >=784.0),
    TEST(lambda precio: precio <1176.0),
    TEST(lambda numeroBaños: numeroBaños >=3),
    TEST(lambda area: area >=160.8),
    TEST(lambda area: area <241.2))
    def pruebaPrecioLaCarolinaBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#FF4633",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una mala compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="San Cristóbal, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio <96.0),
    TEST(lambda precio: precio >=144.0),
    TEST(lambda numeroBaños: numeroBaños <=2),
    TEST(lambda area: area <64.8),
    TEST(lambda area: area >=97.2))
    def pruebaPrecioSanCristóbalBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#49FF33",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una buena compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="San Cristóbal, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio >=96.0),
    TEST(lambda precio: precio <144.0),
    TEST(lambda numeroBaños: numeroBaños >=2),
    TEST(lambda area: area >=64.8),
    TEST(lambda area: area <97.2))
    def pruebaPrecioSanCristóbalBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#FF4633",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una mala compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Roma, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio <92.0),
    TEST(lambda precio: precio >=138.0),
    TEST(lambda numeroBaños: numeroBaños <=1),
    TEST(lambda area: area <45.6),
    TEST(lambda area: area >=68.4))
    def pruebaPrecioRomaBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#49FF33",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una buena compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Roma, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio >=92.0),
    TEST(lambda precio: precio <138.0),
    TEST(lambda numeroBaños: numeroBaños >=1),
    TEST(lambda area: area >=45.6),
    TEST(lambda area: area <68.4))
    def pruebaPrecioRomaBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#FF4633",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una mala compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Pasadena, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio <760.0),
    TEST(lambda precio: precio >=1140.0),
    TEST(lambda numeroBaños: numeroBaños <=4),
    TEST(lambda area: area <151.2),
    TEST(lambda area: area >=226.8))
    def pruebaPrecioPasadenaBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#49FF33",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una buena compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Pasadena, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio >=760.0),
    TEST(lambda precio: precio <1140.0),
    TEST(lambda numeroBaños: numeroBaños >=4),
    TEST(lambda area: area >=151.2),
    TEST(lambda area: area <226.8))
    def pruebaPrecioPasadenaBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#FF4633",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una mala compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="San José de Bavaria, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio <1040.0),
    TEST(lambda precio: precio >=1560.0),
    TEST(lambda numeroBaños: numeroBaños <=4),
    TEST(lambda area: area <345.6),
    TEST(lambda area: area >=518.4))
    def pruebaPrecioSanJosédeBavariaBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#49FF33",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una buena compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="San José de Bavaria, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio >=1040.0),
    TEST(lambda precio: precio <1560.0),
    TEST(lambda numeroBaños: numeroBaños >=4),
    TEST(lambda area: area >=345.6),
    TEST(lambda area: area <518.4))
    def pruebaPrecioSanJosédeBavariaBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#FF4633",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una mala compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="La Floresta, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio <960.0),
    TEST(lambda precio: precio >=660.0),
    TEST(lambda numeroBaños: numeroBaños <=3),
    TEST(lambda area: area <280.0),
    TEST(lambda area: area >=326.4))
    def pruebaPrecioLaFlorestaBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#49FF33",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una buena compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="La Floresta, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio >=960.0),
    TEST(lambda precio: precio <660.0),
    TEST(lambda numeroBaños: numeroBaños >=3),
    TEST(lambda area: area >=280.0),
    TEST(lambda area: area <326.4))
    def pruebaPrecioLaFlorestaBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#FF4633",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una mala compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Los Arrayanes, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio <1056.0),
    TEST(lambda precio: precio >=1584.0),
    TEST(lambda numeroBaños: numeroBaños <=6),
    TEST(lambda area: area <204.0),
    TEST(lambda area: area >=306.0))
    def pruebaPrecioLosArrayanesBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#49FF33",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una buena compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)

    @Rule(Casa(ubicacion="Los Arrayanes, Bogotá",
    precio=MATCH.precio,
    numeroBaños=MATCH.numeroBaños,
    area=MATCH.area),
    TEST(lambda precio: precio >=1056.0),
    TEST(lambda precio: precio <1584.0),
    TEST(lambda numeroBaños: numeroBaños >=6),
    TEST(lambda area: area >=204.0),
    TEST(lambda area: area <306.0))
    def pruebaPrecioLosArrayanesBogotá(self):
        resultado="\nUbicacion: " +str(list(self.facts.get(1).values())[0])+ "\nArea mt2: "+str(list(self.facts.get(1).values())[1])+"\nnumero Baños: "+str(list(self.facts.get(1).values())[2])+ "\nPrecio: "+str(list(self.facts.get(1).values())[3])
        respuesta_label=Label(text=resultado,bg="#FF4633",width="36",heigh="14",font=("Cambria",12))
        respuesta_label.place(x=300,y=70)
        respuesta_label=Label(text="Es una mala compra",bg="#FDFCFB",width="66",heigh="3", font=("Cambria",12))
        respuesta_label.place(x=22,y=430)
def send_data():
    ubicacionD= str(ubicacion_entry.get())
    areaD= str(area_entry.get())
    areaD= float(areaD)
    numeroBañosD= str(numeroBaños_entry.get())
    numeroBañosD= int(numeroBañosD)
    precioD= str(precio_entry.get())
    precioD= float(precioD)
    print(ubicacionD, areaD, numeroBañosD, precioD)
    sugerencia=SugerenciaCasa()
    sugerencia.reset()
    sugerencia.declare(Casa(ubicacion=ubicacionD, area=areaD, numeroBaños=numeroBañosD,precio=precioD))
    sugerencia.run()
myWindows=Tk()
myWindows.geometry("650x650")
myWindows.title("Atilus Desicion")
myWindows.resizable(False,False)
myWindows.config(background ="#121726")
main_title=Label(text="Ingrese los datos",font=("Cambria",13),bg="#146a87",fg="white",width="50",heigh="2")
main_title.pack()

ubicacion_label=Label(text="Ubicacion            ",bg="#1da2c8",fg="white", width=14,font=("Cambria",12))
ubicacion_label.place(x=22,y=70)
area_label=Label(text="Area                    ",bg="#1da2c8",fg="white", width=14,font=("Cambria",12))
area_label.place(x=22,y=130)
numeroBaños_label=Label(text="Numero Baños   ",bg="#1da2c8",fg="white", width=14,font=("Cambria",12))
numeroBaños_label.place(x=22,y=190)
precio_label=Label(text="Precio (Millones)",bg="#1da2c8",fg="white", width=14,font=("Cambria",12))
precio_label.place(x=22,y=250)


ubicacion_Input= StringVar()
area_Input= StringVar()
numeroBaños_Input= StringVar()
precio_Input= StringVar()

ubicacion_entry=Entry(textvariable=ubicacion_Input,width="40")
area_entry=Entry(textvariable=area_Input,width="40")
numeroBaños_entry=Entry(textvariable=numeroBaños_Input,width="40")
precio_entry=Entry(textvariable=precio_Input,width="40")

ubicacion_entry.place(x=22,y=100)
area_entry.place(x=22,y=160)
numeroBaños_entry.place(x=22,y=220)
precio_entry.place(x=22,y=280)

submit_btn =Button(myWindows, text="PROBAR", command=send_data, widt="30", heigh="2", bg= "#20dbd8")
submit_btn.place(x=22 , y =320)

myWindows.mainloop()