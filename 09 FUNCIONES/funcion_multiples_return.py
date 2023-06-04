# En Python, una función puede tener múltiples instrucciones return, pero solo uno de ellos se ejecutará durante la ejecución de la función. Una vez que se encuentra una declaración return, la función finaliza y se devuelve el valor especificado.

def valor(num):
    if num > 0:
        return f"El valor de {num} es positivo"
    elif num < 0:
        return f"El valor de {num} es negativo"
    else:
        return f"{num} es cero"


resultado = valor(0)
print(resultado)
