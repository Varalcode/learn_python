# Escribe un programa en Python que solicite al usuario ingresar una serie de números enteros positivos.
# El programa debe calcular la suma de todos los números ingresados hasta que se ingrese un número negativo.
# Una vez que se ingrese un número negativo, el programa debe imprimir la suma total de los números ingresados.

# Solicitar al usuario que ingrese un número entero positivo
num = int(input("Ingrese un número entero positivo: "))

# Inicializar la variable para almacenar la suma
suma = 0

# Bucle while para sumar los números ingresados hasta que se ingrese un número negativo
while num > 0:
    # Verificar si se ingresó un número negativo y romper el bucle
    if num < 0:
        break
    else:
        # Sumar el número ingresado a la suma total
        suma += num
        # Solicitar al usuario que ingrese otro número entero positivo
        num = int(input("Ingrese un número entero positivo: "))

# Imprimir la suma total de los números ingresados
print(f"La suma de los números enteros positivos ingresados es: {suma}")
