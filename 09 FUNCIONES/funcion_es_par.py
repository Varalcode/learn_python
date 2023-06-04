# Escribe una función llamada "es_par()" que tome un número como entrada y devuelva True si el número es par y False si no lo es.

def es_par(num):
    resultado = True if num % 2 == 0 else False  # operador ternario.
    return resultado


recibe_resultado = es_par(10)
print(recibe_resultado)

recibe_resultado = es_par(15)
print(recibe_resultado)
