def formatear_cadena(texto):
    """
    Función que formatea una cadena de texto.
    Convierte el texto a minúsculas, elimina los espacios en blanco y reemplaza los caracteres acentuados por sus equivalentes sin acento.
    """
    texto = texto.lower().replace(" ", "").replace("á", "a").replace(
        "é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
    return texto


def comparar_cadena(texto):
    """
    Función que compara una cadena de texto con su versión invertida.
    Verifica si el texto ingresado es un palíndromo.
    """
    texto_formateado = formatear_cadena(texto)  # Formatea el texto ingresado
    texto_invertido = texto_formateado[::-1]  # Invierte el texto formateado
    if texto_formateado == texto_invertido:  # Compara el texto formateado con su versión invertida
        print("El texto ingresado es un palíndromo!")
    else:
        print("El texto ingresado no es un palíndromo!")


entrada = input('Ingrese texto: ')  # Solicita al usuario que ingrese un texto
# Compara el texto ingresado con su versión invertida
comparar_cadena(entrada)
