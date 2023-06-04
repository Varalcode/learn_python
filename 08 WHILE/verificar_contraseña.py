# Escribe un programa en Python que solicite al usuario ingresar una contraseña. El programa debe seguir solicitando la contraseña hasta que el usuario ingrese la contraseña correcta. La contraseña correcta es "Python123". Una vez que el usuario ingrese la contraseña correcta, el programa debe imprimir "Contraseña correcta. Acceso concedido" y finalizar.

print("Portal de inicio de sesión.")

contrase_correcta = "Python123"
contrase = input("Ingrese la contraseña: ")

while contrase != contrase_correcta:
    print("Contraseña incorrecta.")
    contrase = input("Ingrese la contraseña: ")

print("Contraseña correcta. Acceso concedido.")
