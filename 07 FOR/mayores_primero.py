# Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el primero.
import sys


def main():
    """Cadena de documentación, también conocida como docstring en inglés."""
    cantidad = int(input("¿Cuántos números va a digitar?: "))

    if cantidad < 1:
        print("La cantidad debe ser mayor a cero.")
        sys.exit()
    else:
        primer_numero = int(input(("Escriba un número: ")))
        for i in range(cantidad):
            numero_2 = int(
                input(f"Escriba un número mayor que {primer_numero}: "))
            if primer_numero >= numero_2:
                print("El número debe ser mayor al anterior.")
    print("Hasta pronto!")


if __name__ == "__main__":
    main()
