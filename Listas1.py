<<<<<<< HEAD:Actividad#2.py
from contextlib import nullcontext

##declaracion de la variables
listaUno=[]
listaDos=[]


def add():
  x=input("DIgite un valor para la lista: ")
  listaUno.append(x)
  print("[",listaUno,"]")



n=True

while True:

  add()

  n=input("Desea continuar agrgando elementos a la lista? (y/n):")
  if n== 'n' or n=='N':
    break

listaDos = listaUno
reverse = listaDos[::-1]
print("[",reverse,"]")
=======
#Crear una lista_uno y adicione elementos en ella hasta que el usuario elija terminar.
#Una vez terminada, crear una segunda lista_dos, en ella llene los valores de lista_uno de forma descentente.

listaUno=[]
listaDos=[]

def add():
  x=input("Digite un valor para la lista: ")
  listaUno.append(x)

n=True

while True:
  add()
  n=input("Desea continuar agrgando elementos a la lista? (y/n):")
  if n== 'n' or n=='N':
    break

listaDos = listaUno
reverse = listaDos[::-1]
print("[",reverse,"]")
>>>>>>> 049abf40dbeaa11ad394c6551169ab1df0843148:Listas1.py
