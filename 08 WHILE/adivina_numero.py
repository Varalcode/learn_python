# Escribe un programa en Python que solicite al usuario adivinar un número secreto.
# El programa generará un número entero aleatorio entre 1 y 20, y el usuario deberá intentar adivinarlo.
# El programa debe proporcionar retroalimentación al usuario indicando si el número ingresado es mayor o menor que el número secreto.
# El programa continuará solicitando al usuario que ingrese un número hasta que adivine correctamente el número secreto.
# Una vez que el usuario adivine correctamente, el programa debe imprimir "¡Felicidades! Has adivinado el número secreto" y
# mostrar la cantidad de intentos realizados.

import random

print("ADIVINA EL NÚMERO SECRETO")

numero_aleatorio = random.randint(1, 20)

num_usuario = int(input("Ingrese un número entre 1 y 20: "))

count = 0

while numero_aleatorio != num_usuario:

    count += 1

    if num_usuario > numero_aleatorio:
        print("Estás frío. Busca más abajo!")
    elif num_usuario < numero_aleatorio:
        print("Estás frío. Busca más arriba!")

    num_usuario = int(input("Ingrese un número entre 1 y 20: "))

print("Felicidades!")
print(f"Lo lograste en {'1' if count == 0 else count+1} intentos!")
