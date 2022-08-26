# Leer una cadena y devolver el numero de palabras de dicha cadena

cadena = str(input("Digite una cadena de palabras --> "))

result = len(cadena.split())

print("Esta cadena tiene " + str(result) + " palabras.")