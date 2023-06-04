# Escribe una función llamada contar_vocales que acepte una cadena de texto como parámetro y cuente el número de vocales (mayúsculas y minúsculas) presentes en esa cadena. La función debe devolver el conteo total de vocales.

def contar_vocales(recibe_cadena):
    """
    Función que cuenta el número de vocales (mayúsculas y minúsculas) en una cadena de texto.
    :param recibe_cadena: Cadena de texto en la cual se contarán las vocales.
    :return: Número total de vocales encontradas en la cadena.
    """
    contador = 0
    for iterador in recibe_cadena:
        if iterador.lower() in "aeiou":
            contador += 1
    return contador


cadena = "De esta cadena de texto se verifica la cantidad de vocales que existen en ella."

# Llama a la función contar_vocales y muestra el resultado
cantidad = contar_vocales(cadena)
print(f'En la cadena de texto: "{cadena}", hay {cantidad} vocales.')
