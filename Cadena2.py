# Leer una cadena y devolver cada palabra de la cadena y el nuemero de veces que se repite

cadenaPalabras=str(input("Digite una cadena de palabras --> "))

listaPalabras = cadenaPalabras.split()

frecuenciaPalab = []
for w in listaPalabras:
    frecuenciaPalab.append(listaPalabras.count(w))

print("Pares\n" + str(list(zip(listaPalabras, frecuenciaPalab))))