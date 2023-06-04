# Escriba un programa que pida dos números enteros positivos e imprima la suma de todos los enteros desde el primer número hasta el segundo.
print("SUMA ENTRE VALORES")


def main():
    """Cadena de documentación, también conocida como docstring en inglés."""

    print("SUMA ENTRE VALORES")

    numero_1 = int(input("Ingrese un número: "))

    if numero_1 < 1:
        print("El número debe ser mayor a cero.")
    else:
        numero_2 = int(input(f"Ingrese un número  mayor que {numero_1}: "))

    if numero_2 <= numero_1:
        print(f"El segundo número debe ser mayor a {numero_1}.")
    else:
        suma = 0

        for i in range(numero_1, numero_2+1):
            suma += i
        print(f"La suma desde {numero_1} hasta {numero_2} es: {suma}")


if __name__ == "__main__":
    main()
