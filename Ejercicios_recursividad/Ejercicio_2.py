# Ejericio 2: Función Fibonacci

# Escribe una función recursiva que calcule el n-ésimo término de la secuencia de Fibonacci.

#SOLUCION 1

def fibo (n):
    if n in (0,1):
        return 1
    else:
        return fibo (n - 1) + fibo (n - 2)

print(fibo(7))


