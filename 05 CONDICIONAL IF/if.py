# El código se ejecuta de arriba hacia abajo y en el momento en que se cumpla la condición deja de ejecutarse la condición if.

edad = 15

if edad > 50:
    print('Puedes ver la película con descuento.')
elif edad >= 18:
    print('Puedes ver la película.')
# La instrucción elif debe ir al  mismo nivel de if al igual que la instrucción else.
else:
    print('No puedes ver la película.')
