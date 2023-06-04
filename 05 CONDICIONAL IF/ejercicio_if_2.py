# Escribe un programa que tome una lista de números como entrada y calcule la suma de todos los números pares en la lista. Luego, muestra el resultado por pantalla. Puedes utilizar estructuras de control como el condicional "if" y bucles para resolver este ejercicio.
lista_num = [2, 4, 7, 9, 15, 4]
suma_pares = 0

for iterador_numero in lista_num:
    if iterador_numero % 2 == 0:
        suma_pares += iterador_numero
print(f"La suma de los números pares de  la lista es {suma_pares}.")
