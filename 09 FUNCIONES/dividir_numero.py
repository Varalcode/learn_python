def dividir_numero(numero, divisor):
    """
    Función que divide un número por otro y devuelve el cociente y el residuo.
    :param numero: Número a dividir.
    :param divisor: Número divisor.
    :return: Tupla con el cociente y el residuo.
    """
    cociente = numero // divisor
    residuo = numero % divisor
    return cociente, residuo


# Ejemplo de uso de la función
num = 20
div = 7

resultado = dividir_numero(num, div)
# El retorno (que es la variable resultado) llega en forma de tupla y luego yo puedo acceder de manera independiente a sus dos valores con las variables cociente y residuo.
cociente, residuo = resultado

print(f"El cociente de {num} dividido por {div} es: {cociente}")
print(f"El residuo de {num} dividido por {div} es: {residuo}")
