# Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.

import sys


def main():
    """Cadena de documentación, también conocida como docstring en inglés."""
    print("DIVISORES")

    # Solicita un número entero y lo asigna a la variable numero.
    numero = int(input("Escriba un número entero mayor que cero: "))

    # Con el if se verifica que el número ingresado sea mayor a cero.
    if numero <= 0:
        print("¡Le he pedido un número entero mayor que cero!")
        sys.exit()  # Función que finaliza la ejecución del programa.
    else:
        # En este bloque de código se realiza la operación de verificar los números divisores del número ingresado.
        print(f"Los divisores de {numero} son ", end="")
        for i in range(1, numero // 2 + 1):
            if numero % i == 0:
                print(i, end=" ")
        print(f"{numero} ")


if __name__ == "__main__":
    main()
