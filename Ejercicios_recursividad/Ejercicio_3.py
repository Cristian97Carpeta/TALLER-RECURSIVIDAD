# Ejercicio 3: Función de Ackermann

# Escribe una función recursiva que calcule la función de Ackermann.


# SOLUCION 1

def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann (m - 1, 1)
    else:
        return ackermann (m - 1,ackermann(m, n - 1))

valor = ackermann(m = 2,n = 3)
print("el resultado es", valor)


# SOLUCION 2

def ackermann(m, n):
    # Caso base: A(m, n) = n + 1 si m = 0
    if m == 0:
        return n + 1
    # Caso recursivo: A(m, n) = A(m-1, 1) si m > 0 y n = 0
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    # Caso recursivo: A(m, n) = A(m-1, A(m, n-1)) si m > 0 y n > 0
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))

# Ejemplo de uso
m = 2
n = 3
print(f"A({m}, {n}) = {ackermann(m, n)}")
