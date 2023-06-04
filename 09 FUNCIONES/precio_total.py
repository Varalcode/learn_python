def calcular_precio_total(producto, precio_unitario, cantidad):
    """
    Función que calcula el precio total de un producto dado su precio unitario y la cantidad.
    :param producto: Nombre del producto.
    :param precio_unitario: Precio unitario del producto.
    :param cantidad: Cantidad del producto a comprar.
    :return: Precio total del producto.
    """
    precio_total = precio_unitario * cantidad
    return precio_total


# Ejemplo de uso de la función
nombre_producto = "Camiseta"
precio = 25.99
cantidad_producto = 3

total = calcular_precio_total(nombre_producto, precio, cantidad_producto)
print(
    f"El precio total de {cantidad_producto} {nombre_producto}(s) es: ${total}")
