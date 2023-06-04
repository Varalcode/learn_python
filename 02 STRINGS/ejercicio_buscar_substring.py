# Buscar una subcadena o substring dentro de una cadena de texto.

mensaje = 'Hola, ¿Cómo estás?'

# Esta instrucción con el método find() retorna la posición desde donde inicia la subcadena de texto buscada.
print(mensaje.find('ola'))

# Esta instrucción verifica si una subcadena de texto se encuentra dentro de un string.

if 'ola' in mensaje:

    # Si esa condición se cumple (si el substring ola se encuentra en la cadena de texto
    # mensaje), se ejecuta el bloque de código que está dentro de la condición.
    # Se puede ejecutar cualquier código que se requiera.

    nueva_variable = f'El substring ola sí se encuentra en la cadena de texto: "{mensaje}"'

print(nueva_variable)

# De la siguiente manera retorna el valor True o False dependiendo si está o no el substring.
print('ola' in mensaje)
