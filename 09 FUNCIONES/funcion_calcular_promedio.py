from statistics import mean

lista = [2, 4, 11]


def calcular_promedio(parametro):
    promedio = mean(parametro)
    return promedio


promedio_calculado = calcular_promedio(lista)
print(promedio_calculado)
