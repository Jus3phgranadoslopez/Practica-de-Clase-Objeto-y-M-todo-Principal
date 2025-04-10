class Estudiante:
    def __init__(self, nombre, edad, calificacion):
        """
        Constructor de la clase Estudiante.

        Args:
            nombre (str): El nombre del estudiante.
            edad (int): La edad del estudiante.
            calificacion (float): La calificación del estudiante.
        """
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    def mostrar_informacion(self):
        """
        Muestra la información del estudiante (nombre, edad y calificación).
        """
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Calificación: {self.calificacion}")

    def ha_aprobado(self, calificacion_minima=6.0):
        """
        Verifica si el estudiante ha aprobado basándose en su calificación.

        Args:
            calificacion_minima (float): La calificación mínima para aprobar (por defecto es 6.0).

        Returns:
            bool: True si el estudiante aprobó, False si reprobó.
        """
        return self.calificacion >= calificacion_minima


estudiante1 = Estudiante("Ana Pérez", 20, 8.5)
estudiante2 = Estudiante("Carlos López", 19, 5.2)

estudiante1.mostrar_informacion()
if estudiante1.ha_aprobado():
    print(f"{estudiante1.nombre} ha aprobado.")
else:
    print(f"{estudiante1.nombre} ha reprobado.")

print("\n")

estudiante2.mostrar_informacion()
if estudiante2.ha_aprobado(calificacion_minima=7.0): # Ejemplo con otra calificación mínima
    print(f"{estudiante2.nombre} ha aprobado.")
else:
    print(f"{estudiante2.nombre} ha reprobado.")