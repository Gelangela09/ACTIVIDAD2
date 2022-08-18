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
