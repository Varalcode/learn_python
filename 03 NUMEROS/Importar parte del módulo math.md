## Response:
Sí, es posible importar solo una parte específica del módulo `math` en lugar de importar todo el módulo. Esto se hace utilizando la declaración `from ... import`.

Aquí tienes un ejemplo de cómo importar solo la función `sqrt()` del módulo `math`:

```python
from math import sqrt

numero = 16
raiz_cuadrada = sqrt(numero)

print("Raíz cuadrada de", numero, "es:", raiz_cuadrada)
```

En este caso, solo hemos importado la función `sqrt()` del módulo `math`. Esto significa que puedes usar directamente `sqrt()` en tu código sin tener que hacer referencia al módulo `math`.

Del mismo modo, puedes importar otras funciones o constantes específicas del módulo `math` utilizando la misma sintaxis. Por ejemplo:

```python
from math import sin, cos, pi

angulo = pi / 4
seno = sin(angulo)
coseno = cos(angulo)

print("Seno:", seno)
print("Coseno:", coseno)
```

En este caso, hemos importado las funciones `sin()` y `cos()` junto con la constante `pi` del módulo `math`.

Importar solo las partes necesarias de un módulo puede ser útil para evitar colisiones de nombres y hacer que el código sea más legible. Sin embargo, si necesitas usar varias funciones o constantes del módulo `math`, puede ser más conveniente importar todo el módulo utilizando `import math`.

Recuerda que, al importar solo partes específicas del módulo, ya no necesitarás hacer referencia al nombre del módulo al usar esas partes.

