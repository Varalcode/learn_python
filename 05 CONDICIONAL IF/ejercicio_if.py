# Escribe un programa que solicite al usuario ingresar un número. El programa debe imprimir un mensaje indicando si el número ingresado es positivo, negativo o cero.
num = int(input('Ingrese un número: '))

if num > 0:
    print('El número ingresado en positivo!')
elif num < 0:
    print('El número ingresado en negativo!')
else:
    print('El número ingresado es el cero!')
