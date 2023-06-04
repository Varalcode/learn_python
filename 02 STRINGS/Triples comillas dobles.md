## Prompt:
Para que se usan las triples comillas dobles en Python?

## Response:
En Python, las triples comillas dobles (`"""`) se utilizan para crear cadenas de texto multilínea, también conocidas como cadenas de texto de varias líneas o docstrings. Las triples comillas dobles permiten crear cadenas de texto que abarcan varias líneas sin necesidad de utilizar caracteres de escape.

Las triples comillas dobles son especialmente útiles en los siguientes casos:

1. Docstrings: Las triples comillas dobles se utilizan para crear documentación en forma de cadenas de texto dentro de funciones, clases o módulos. Los docstrings proporcionan información sobre el propósito, la funcionalidad y el uso de una determinada función, clase o módulo. Pueden ser accedidos a través del atributo `__doc__`.

2. Texto largo: Si necesitas crear una cadena de texto que ocupe varias líneas, puedes utilizar las triples comillas dobles en lugar de concatenar múltiples cadenas o utilizar caracteres de escape como `\n` para insertar saltos de línea.

3. Comentarios largos: Las triples comillas dobles también se pueden usar para crear comentarios largos que abarquen varias líneas. Aunque no se recomienda utilizar comentarios largos en el código, en ocasiones puede ser útil para explicar secciones de código complejas o realizar anotaciones extensas.

Aquí tienes un ejemplo de cómo se utilizan las triples comillas dobles para crear un docstring:

```python
def calcular_promedio(valores):
    """Calcula el promedio de una lista de valores.

    Argumentos:
    - valores: una lista de números.

    Retorna:
    - El promedio de los valores en la lista.
    """
    total = sum(valores)
    promedio = total / len(valores)
    return promedio
```

En este ejemplo, el docstring proporciona información sobre los argumentos de la función, lo que devuelve y cualquier otra información relevante.

