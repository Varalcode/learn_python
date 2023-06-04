# Escribe una función llamada contar_vocales que acepte una cadena de texto como parámetro y cuente el número de vocales (mayúsculas y minúsculas) presentes en esa cadena. La función debe devolver el conteo total de vocales.

def contar_vocales2(recibe_cadena):
    """
    Función que cuenta el número de vocales (mayúsculas y minúsculas) en una cadena de texto.
    :parametro recibe_cadena: Cadena de texto en la cual se contarán las vocales.
    :return: Número total de vocales encontradas en la cadena.
    """
    contador = recibe_cadena.lower().count("a")+recibe_cadena.lower().count("e") + \
        recibe_cadena.lower().count("i")+recibe_cadena.lower().count("o") + \
        recibe_cadena.lower().count("u")
    return contador


cadena = "De esta cadena de texto se verifica la cantidad de vocales que existen en ella."

# Llama a la función contar_vocales2 y muestra el resultado
cantidad = contar_vocales2(cadena)
print(
    f'SEGUNDA MANERA: En la cadena de texto: "{cadena}", hay {cantidad} vocales.')
