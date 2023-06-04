# Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el anterior.
import sys


def main():
    """Cadena de documentación, también conocida como docstring en inglés."""
    cantidad = int(input("¿Cuántos números va a digitar?: "))

    if cantidad < 1:
        print("La cantidad debe ser mayor a cero.")
        sys.exit()
    else:
        for i in range(cantidad):
            numero_anterior = int(input(("Escriba un número: ")))
            numero_2 = int(
                input(f"Escriba un número mayor que {numero_anterior}: "))
            if numero_anterior >= numero_2:
                print("El número debe ser mayor al anterior.")
    print("Hasta pronto!")


if __name__ == "__main__":
    main()
