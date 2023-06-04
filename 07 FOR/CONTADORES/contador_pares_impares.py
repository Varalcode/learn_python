# Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y diga al final cuántos han sido pares y cuántos impares.
def main():
    """Cadena de documentación, también conocida como docstring en inglés."""

    cantidad = int(input("Ingrese la cantidad de números a digitar: "))

    if cantidad < 1:
        print("Por favor ingrese un número mayor a cero.")
    else:

        suma_pares = 0
        suma_impares = 0

        for i in range(1, cantidad+1):

            numeros = int(input(f"Ingrese el número {i} a evaluar: "))

            if numeros % 2 == 0:
                suma_pares += 1
            else:
                suma_impares += 1

        print(
            f"{'Se encontró' if suma_pares == 1 else 'Se encontraron'} {suma_pares}", end=" ")
        print(f"{'número par' if suma_pares == 1 else 'números pares'}", end=" ")

        print(
            f"{'y se encontró' if suma_impares == 1 else 'y se encontraron'} {suma_impares}", end=" ")
        print(f"{'número impar' if suma_impares == 1 else 'números impares'}")

    print("FIN DEL PROGRAMA!")


if __name__ == "__main__":
    main()
