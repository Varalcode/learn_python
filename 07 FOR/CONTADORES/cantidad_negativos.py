# Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.

def main():
    """Cadena de documentación, también conocida como docstring en inglés."""

    cantidad = int(input("Ingrese la cantidad de números a digitar: "))

    if cantidad < 1:
        print("El número debe ser mayor a cero.")
    else:
        num_negativos = 0
        for i in range(1, cantidad+1):
            numeros = int(input(f"Ingrese el número {i}: "))
            if numeros < 0:
                num_negativos += 1
        print(
            f"Ha ingresado {num_negativos} {'número negativo' if num_negativos == 1 else 'numeros negativos'}.")


if __name__ == "__main__":
    main()
