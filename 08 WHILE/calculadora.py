print("BIENVENIDO A LA CALCULADORA")
print("Escriba salir para abandonar el programa.")

resultado = ""

while True:
    if not resultado:
        resultado = input("Ingrese un número: ")
        if resultado.lower() == 'salir':
            break
        resultado = int(resultado)

    op = input("Ingrese el símbolo de la operación: ")
    if op.lower() == 'salir':
        break

    n2 = input("Ingrese el siguiente número: ")
    if n2.lower() == 'salir':
        break
    n2 = int(n2)

    if op.lower() == 'suma':
        resultado += n2
    elif op.lower() == 'resta':
        resultado -= n2
    elif op.lower() == 'multi':
        resultado *= n2
    elif op.lower() == 'div':
        resultado /= n2
    else:
        print('Operación no válida.')
        break

    print(f"El resultado es {resultado}")
