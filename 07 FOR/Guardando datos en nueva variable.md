## Response:
¡Claro! Aquí tienes un ejemplo en el cual almacenaremos los resultados de cada iteración en una nueva lista:

```python
numeros = [1, 2, 3, 4, 5]
cuadrados = []

for num in numeros:
    cuadrado = num ** 2
    cuadrados.append(cuadrado)

print(cuadrados)
```

En este ejemplo, tenemos una lista llamada "numeros" que contiene algunos números. Queremos calcular el cuadrado de cada número y almacenar los resultados en una nueva lista llamada "cuadrados".

Dentro del bucle "for", la variable "num" tomará el valor de cada número en cada iteración. Luego, calculamos el cuadrado de "num" usando el operador de exponente (\*\*) y lo almacenamos en la variable "cuadrado". Después, usamos el método "append()" para agregar "cuadrado" a la lista "cuadrados".

Al finalizar el bucle, imprimimos la lista "cuadrados" que contiene los resultados de cada iteración.

La salida será:

```csharp
[1, 4, 9, 16, 25]
```

En este caso, hemos almacenado los cuadrados de los números del 1 al 5 en la lista "cuadrados". Puedes modificar la lista "numeros" o utilizar otras secuencias según tus necesidades.

Recuerda que al utilizar el método "append()", estás agregando cada resultado al final de la lista. Si deseas almacenar los resultados en un orden diferente, deberás ajustar el código en consecuencia.

¡Espero que este ejemplo te sea útil! Si tienes alguna pregunta adicional, no dudes en hacerla.

