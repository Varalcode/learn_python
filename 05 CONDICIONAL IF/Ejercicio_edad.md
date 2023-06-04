## Prompt:
Realiza el siguiente ejercicio en lenguaje de programación Python y me explicas el código: Un programa que reciba un número entero y lo asigna a la variable edad. Si esa edad es mayor o igual a 65 imprime "Es mayor o igual a 65 años", si es mayor o igual a 50 imprime "Es mayor o igual a 50 años", si es mayor o igual a 18 imprime "Es mayor o igual a 18 años" y si es menor a 18 imprime "Es menor de 18 años".

## Response:
Por supuesto, aquí tienes el código en Python que cumple con los requisitos mencionados:

```python
edad = int(input("Ingrese su edad: "))

if edad >= 65:
    print("Es mayor o igual a 65 años")
elif edad >= 50:
    print("Es mayor o igual a 50 años")
elif edad >= 18:
    print("Es mayor o igual a 18 años")
else:
    print("Es menor de 18 años")
```

Explicación del código:

1. Al igual que en el ejercicio anterior, la línea `edad = int(input("Ingrese su edad: "))` solicita al usuario ingresar su edad y la almacena en la variable `edad`. La función `input` se utiliza para leer la entrada del usuario como una cadena de texto, y luego `int()` se utiliza para convertir esa cadena en un número entero.

2. La estructura condicional `if-elif-else` se utiliza para evaluar diferentes condiciones y ejecutar el código correspondiente según el resultado.

3. La primera condición `if edad >= 65` verifica si la edad es mayor o igual a 65. Si es cierto, se imprime "Es mayor o igual a 65 años".

4. Si la primera condición no se cumple, se evalúa la segunda condición `elif edad >= 50` para verificar si la edad es mayor o igual a 50. Si es cierto, se imprime "Es mayor o igual a 50 años".

5. Si ambas condiciones anteriores no se cumplen, se evalúa la tercera condición `elif edad >= 18` para verificar si la edad es mayor o igual a 18. Si es cierto, se imprime "Es mayor o igual a 18 años".

6. Si ninguna de las condiciones anteriores se cumple, se ejecuta el bloque `else` y se imprime "Es menor de 18 años". Esto significa que si la edad es menor a 18, se mostrará este mensaje.

El programa evaluará la edad ingresada por el usuario y mostrará el mensaje correspondiente según la condición que se cumpla.
