class Producto:
    def __init__(self, nombre, precio, stock):
        """
        Constructor de la clase Producto.

        Args:
            nombre (str): El nombre del producto.
            precio (float): El precio unitario del producto.
            stock (int): La cantidad disponible en stock.
        """
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def verificar_disponibilidad(self, cantidad):
        """
        Verifica si hay suficiente stock para la cantidad solicitada.

        Args:
            cantidad (int): La cantidad que se desea verificar.

        Returns:
            bool: True si hay suficiente stock, False en caso contrario.
        """
        return self.stock >= cantidad

    def vender(self, cantidad):
        """
        Reduce el stock si hay disponibilidad o muestra un mensaje de falta de stock.

        Args:
            cantidad (int): La cantidad que se desea vender.
        """
        if self.verificar_disponibilidad(cantidad):
            self.stock -= cantidad
            print(f"Se vendieron {cantidad} unidades de '{self.nombre}'. Stock actual: {self.stock}")
        else:
            print(f"No hay suficiente stock de '{self.nombre}' para vender {cantidad} unidades. Stock actual: {self.stock}")

    def reabastecer(self, cantidad):
        """
        Aumenta el stock del producto.

        Args:
            cantidad (int): La cantidad con la que se va a reabastecer.
        """
        if isinstance(cantidad, int) and cantidad > 0:
            self.stock += cantidad
            print(f"Se reabastecieron {cantidad} unidades de '{self.nombre}'. Stock actual: {self.stock}")
        else:
            print("Error: La cantidad para reabastecer debe ser un entero positivo.")

# Crear un objeto Producto con los valores iniciales
laptop = Producto("Laptop", 1200, 10)

# Realizar las operaciones solicitadas
print(f"Producto: {laptop.nombre}, Precio: ${laptop.precio}, Stock: {laptop.stock}\n")

#Verificar si hay 5 unidades disponibles
cantidad_verificar1 = 5
disponible1 = laptop.verificar_disponibilidad(cantidad_verificar1)
print(f"¿Hay {cantidad_verificar1} unidades de '{laptop.nombre}' disponibles? {disponible1}")

#Vender 3 unidades
cantidad_vender1 = 3
laptop.vender(cantidad_vender1)

#Verificar si hay 8 unidades disponibles
cantidad_verificar2 = 8
disponible2 = laptop.verificar_disponibilidad(cantidad_verificar2)
print(f"¿Hay {cantidad_verificar2} unidades de '{laptop.nombre}' disponibles? {disponible2}")

#Intentar vender 8 unidades (debe fallar)
cantidad_vender_fallida = 8
laptop.vender(cantidad_vender_fallida)

#Reabastecer con 10 unidades adicionales
cantidad_reabastecer = 10
laptop.reabastecer(cantidad_reabastecer)

#Verificar nuevamente si hay 8 unidades disponibles
cantidad_verificar3 = 8
disponible3 = laptop.verificar_disponibilidad(cantidad_verificar3)
print(f"¿Hay {cantidad_verificar3} unidades de '{laptop.nombre}' disponibles? {disponible3}")

#Vender 8 unidades
cantidad_vender2 = 8
laptop.vender(cantidad_vender2)

print(f"\nStock final de '{laptop.nombre}': {laptop.stock}")