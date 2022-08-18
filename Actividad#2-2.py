#Crear una lista con los elemntos de los numeros de la Serie de Fibonacci

# Partiendo con los nuemeros inicales [0, 1].

# Obtener la serie [0, 1, 1, 2, 3, 5, 8, 13, 21, ..... ]
def rec_fib(n):
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n
for i in range(10):
    print(rec_fib(i))