# requests: permite descargar archivos
# os: se ultiliza para poder interactuar con el sistema operativo
# Image: serie de funciones de fábrica, funciones para cargar imágenes desde archivos y crear nuevas imágenes.
# IFrame: es un elemento HTML que permite renderizar un documento dentro de otro documento HTML en una página web.
from fileinput import close
import requests
import os 
from PIL import Image
from IPython.display import IFrame
#get() recupera la informacion del sevidor
#post() envia la informacion del servidor
#put() actualiza los datos del sevidor en tiempo real
#delete() borra la informacion del servidor
url='https://www.ibm.com/'
r=requests.get(url)
print("status code: \n",r.status_code)
print("request headers: \n",r.request.headers)
print("request body:\n", r.request.body)
header=r.headers
print("r.headers \n",r.headers)
print("header[date]\n",header['date'])
print("header['Content-Type']\n",header['Content-Type'])
print("r.encoding\n",r.encoding)
print("r.text[0:100]\n",r.text[0:100])
#load otrher type of data
url='https://empresas.blogthinkbig.com/wp-content/uploads/2019/11/Imagen3-245003649.jpg?w=800'
r=requests.get(url)
print("r.headers\n",r.headers)
print("r.headers['Content-Type']\n",r.headers['Content-Type'])
# Este método concatena varios componentes de la ruta con exactamente un separador de directorio ('/') después de cada parte no vacía,
path=os.path.join(os.getcwd(),'image.png')
with open(path,'wb') as f:
    f.write(r.content)
    print("path \n", path)
imagen=Image.open(path)
imagen.show()    
print("Metodos que puede usar image: %s" %dir(imagen))
f.close()    
#-------------------------------------------------------------
#Get Request with URL Parameters     
#---------------------------------------------------------------
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path=os.path.join(os.getcwd(),'example1.txt')
r=requests.get(url)
with open(path,'wb') as f:
    f.write(r.content)
url_get='http://httpbin.org/get'
payload={"name":"Joseph","ID":"123"}
r=requests.get(url_get,params=payload)
print(r.url)
print("request body\n", r.request.body)
print("r.status_code\n",r.status_code)
print("r.text\n",r.text)
print("r.headers['Content-Type']\n",r.headers['Content-Type'])
print("r.json()\n",r.json())
print("r.json()['args']\n",r.json()['args'])

#-----------------------------------------------------
#Post Requests 
#----------------------------------------------------
url_post='http://httpbin.org/post'
r_post=requests.post(url_post,data=payload)
print("POST request URL:\n",r_post.url ,"\n")
print("GET request URL:\n",r.url,"\n")
print("POST request body:\n",r_post.request.body,"\n")
print("GET request body:\n",r.request.body,"\n")
print("r_post.json()['form']\n",r_post.json()['form'],"\n")
    
    


