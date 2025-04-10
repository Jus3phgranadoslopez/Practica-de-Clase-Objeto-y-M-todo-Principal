class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima):
        """
        Constructor de la clase Vehiculo.

        Args:
            marca (str): La marca del vehículo.
            modelo (str): El modelo del vehículo.
            velocidad_maxima (int): La velocidad máxima del vehículo en km/h.
        """
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0

    def acelerar(self, incremento):
        """
        Aumenta la velocidad actual del vehículo sin superar la velocidad máxima.

        Args:
            incremento (int): La cantidad en km/h a aumentar la velocidad.
        """
        if incremento > 0:
            self.velocidad_actual += incremento
            if self.velocidad_actual > self.velocidad_maxima:
                self.velocidad_actual = self.velocidad_maxima
                print(f"¡Alcanzó la velocidad máxima ({self.velocidad_maxima} km/h)! Velocidad actual: {self.velocidad_actual} km/h")
            else:
                print(f"Acelerando. Velocidad actual: {self.velocidad_actual} km/h")
        else:
            print("El incremento de velocidad debe ser positivo.")

    def frenar(self, decremento):
        """
        Reduce la velocidad actual del vehículo sin bajar de 0.

        Args:
            decremento (int): La cantidad en km/h a reducir la velocidad.
        """
        if decremento > 0:
            self.velocidad_actual -= decremento
            if self.velocidad_actual < 0:
                self.velocidad_actual = 0
                print("El vehículo se ha detenido. Velocidad actual: 0 km/h")
            else:
                print(f"Frenando. Velocidad actual: {self.velocidad_actual} km/h")
        else:
            print("El decremento de velocidad debe ser positivo.")

    def verificar_limite(self, velocidad_limite):
        """
        Verifica si la velocidad actual del vehículo supera un límite dado.

        Args:
            velocidad_limite (int): El límite de velocidad a verificar en km/h.
        """
        if self.velocidad_actual > velocidad_limite:
            print(f"¡Advertencia! El vehículo está excediendo el límite de velocidad de {velocidad_limite} km/h. Velocidad actual: {self.velocidad_actual} km/h")
        else:
            print(f"El vehículo está dentro del límite de velocidad de {velocidad_limite} km/h. Velocidad actual: {self.velocidad_actual} km/h")

#menú interactivo
if __name__ == "__main__":
    marca_vehiculo = input("Ingrese la marca del vehículo: ")
    modelo_vehiculo = input("Ingrese el modelo del vehículo: ")
    try:
        velocidad_maxima_vehiculo = int(input("Ingrese la velocidad máxima del vehículo (km/h): "))
        mi_vehiculo = Vehiculo(marca_vehiculo, modelo_vehiculo, velocidad_maxima_vehiculo)
        print(f"\nVehículo creado: {mi_vehiculo.marca} {mi_vehiculo.modelo}, Velocidad máxima: {mi_vehiculo.velocidad_maxima} km/h")

        while True:
            print("\n--- Menú ---")
            print("1. Acelerar")
            print("2. Frenar")
            print("3. Verificar límite de velocidad")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                try:
                    incremento = int(input("Ingrese la cantidad a acelerar (km/h): "))
                    mi_vehiculo.acelerar(incremento)
                except ValueError:
                    print("Por favor, ingrese un valor numérico para el incremento.")
            elif opcion == '2':
                try:
                    decremento = int(input("Ingrese la cantidad a frenar (km/h): "))
                    mi_vehiculo.frenar(decremento)
                except ValueError:
                    print("Por favor, ingrese un valor numérico para el decremento.")
            elif opcion == '3':
                try:
                    limite = int(input("Ingrese el límite de velocidad a verificar (km/h): "))
                    mi_vehiculo.verificar_limite(limite)
                except ValueError:
                    print("Por favor, ingrese un valor numérico para el límite de velocidad.")
            elif opcion == '4':
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción del menú.")

    except ValueError:
        print("Error: La velocidad máxima debe ser un número entero.")