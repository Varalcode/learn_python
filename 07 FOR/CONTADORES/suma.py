# Escriba un programa que pregunte cuantos números se van a introducir, pida esos números (que puedan ser decimales) y calcule su suma.

def main():
    """Cadena de documentación, también conocida como docstring en inglés."""

    cantidad = int(input("Ingrese la cantidad de números a digitar: "))

    if cantidad < 1:
        print("Por  favor ingrese un número mayor a 0.")
    else:
        suma = 0
        for i in range(1, cantidad+1):
            numeros = float(input(f"Ingrese el número {i}: "))
            suma = suma + numeros

    print(
        f"La suma de todos los números es {int(suma)if suma % 2 == 0 else suma:.2f}")


if __name__ == "__main__":
    main()
