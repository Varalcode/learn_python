# El "if ternario" o "operador ternario" en Python es una forma concisa de escribir una expresión condicional en una sola línea. También se conoce como "operador condicional" o "operador inline if".

# El operador ternario tiene la siguiente sintaxis:

# valor_verdadero if condición else valor_falso

# Aquí, condición es una expresión booleana que se evalúa como Verdadero o Falso. Si la condición es Verdadero, se devuelve valor_verdadero. En caso contrario, se devuelve valor_falso.

# La ventaja de utilizar el operador ternario es que permite escribir expresiones condicionales de forma más concisa y legible, especialmente cuando se requiere una simple evaluación condicional sin necesidad de un bloque completo de instrucciones if-else.

# Aquí tienes un ejemplo que muestra cómo utilizar el operador ternario:

edad = 20
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)

# En este caso, se evalúa la condición edad >= 18. Si es Verdadero, se asigna el valor "Mayor de edad" a mensaje. Si es Falso, se asigna el valor "Menor de edad". El resultado se imprime en la consola.

# El operador ternario es especialmente útil cuando se desea asignar un valor a una variable en función de una condición, todo en una sola línea.

# Otro ejemplo:

num = 0
resultado = 2+5 if num != 0 else f"No hay operación porque {num} es cero"
print(resultado)

# Es importante tener en cuenta que el uso excesivo del operador ternario puede dificultar la legibilidad del código, especialmente cuando las expresiones condicionales son complejas. En esos casos, es preferible utilizar el enfoque convencional con instrucciones if-else.
