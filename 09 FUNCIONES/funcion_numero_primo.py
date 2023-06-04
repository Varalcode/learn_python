def numero_primo(num):
    if num > 0 and num != 2 and num % 2 == 0:
        return 'El número no es primo'
    else:
        return 'El número es primo'


resultado = numero_primo(53)
print(resultado)
