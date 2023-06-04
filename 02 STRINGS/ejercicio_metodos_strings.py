pais = '    colombia Tierra quERida   '
# Convierte todas las letras a mayúsculas.
print(pais.upper())

# Convierte todas las letras a minúsculas.
print(pais.lower())

# Convierte la primera letra del texto en mayúscula y todas las demás en minúsculas.
# Se pueden unir métodos para ejecutar varias acciones al mismo tiempo.
print(pais.strip().capitalize())

# Convierte la  primera letra de cada palabra en mayúscula y las demás en minúsculas.
print(pais.title())

# Elimina todos los espacios en blanco al comienzo y al final del texto.
print(pais.strip())

# Elimina todos los espacios en blanco al comienzo del texto.
print(pais.lstrip())

# Elimina todos los espacios en blanco al final del texto.
print(pais.rstrip())

# Busca un caracter o una cadena de caracteres según lo que nosotros  le ordenemos.
print(pais.find("b"))

# Reemplaza los caracteres que indiquemos.
print(pais.replace("b", "v"))
