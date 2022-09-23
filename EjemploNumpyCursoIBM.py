import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt
# plt.axes() : Agregue un eje a la figura actual y conviértalo en los ejes actuales
# ax.arrow() ; Crea el vecctor con los siguientes parametros(centro,parametro en x,parametro en y,color,
# plt.trxt() : Agregue el texto s a los ejes en la ubicación x , y en coordenadas de datos
#              ((longitud, altura), texto) 
def Plotvec1(u, z, v):
    
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1) 
    plt.text(*(u + 0.1), 'u')
    
    ax.arrow(0, 0, *v ,head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

def Plotvec2(a,b):
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

u=np.array([1,0])
v=np.array([0,1])
z=u+v
Plotvec1(u, z, v)
plt.show()