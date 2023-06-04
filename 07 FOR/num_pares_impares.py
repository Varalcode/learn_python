# Escriba un programa que pida dos números enteros e imprima qué números son pares y cuáles impares desde el primero hasta el segundo.
import sys


def main():
    # Una cadena de documentación, también conocida como docstring en inglés, es una cadena de texto que se utiliza para documentar funciones, clases, módulos u otros objetos en Python. La cadena de documentación se encuentra en la primera línea después de la declaración del objeto y está delimitada por triples comillas.
    """
    Evalúa qué números son pares e impares en un rango determinado por dos números
    enteros que recibe.

    Args:
        Esta función no recibe argumentos.

    Returns:
        Esta función no retorna valores.
    """

    print('PARES E IMPARES')
    num_1 = int(input('Ingrese un número entero: '))
    num_2 = int(
        input(f'Ingrese un número entero mayor o igual que {num_1}: '))

    # Verifica si el segundo número ingresado es mayor al primero.
    if num_2 < num_1:
        print('El número 2 debe ser menor al número 1')
        sys.exit()

    for iterable in range(num_1, num_2+1):
        if iterable % 2 == 0:
            print(f"El número {iterable} es par.")
        else:
            print(f"El número {iterable} es impar.")


if __name__ == "__main__":
    main()
