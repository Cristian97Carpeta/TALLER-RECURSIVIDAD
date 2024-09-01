# Ejercicio 1: Función potencia


# Escribe una función recursiva que calcule la potencia de un número entero positivo x elevado a un número entero positivo y.

# SOLUCIÓN 1

def potencia (n, m):

    if m > 0:
        return n * potencia(n , m - 1)

    else:
        return 1

print (potencia (3, 3))

# SOLUCIÓN 2

def potencia(x, y):

    if y == 0:
        return 1
    else:
        return x * potencia(x, y - 1)

resultado = potencia(2, 3)
print(resultado)

