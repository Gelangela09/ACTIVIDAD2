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