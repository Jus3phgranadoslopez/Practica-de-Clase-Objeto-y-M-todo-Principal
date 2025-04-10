
class Libro:
    def __init__(self, titulo, autor, num_paginas):
        """
        Constructor de la clase Libro.

        Args:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            num_paginas (int): El número de páginas del libro.
        """
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def mostrar_informacion(self):
        """
        Muestra la información del libro (título, autor y número de páginas).
        """
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.num_paginas}")

    def actualizar_num_paginas(self, nuevo_num_paginas):
        """
        Actualiza el número de páginas del libro.

        Args:
            nuevo_num_paginas (int): El nuevo número de páginas.
        """
        if isinstance(nuevo_num_paginas, int) and nuevo_num_paginas >= 0:
            self.num_paginas = nuevo_num_paginas
            print(f"El número de páginas de '{self.titulo}' ha sido actualizado a {self.num_paginas}.")
        else:
            print("Error: El número de páginas debe ser un entero no negativo.")


libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 496)
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 96)

libro1.mostrar_informacion()
print("\n")
libro2.mostrar_informacion()

libro1.actualizar_num_paginas(500)
libro2.actualizar_num_paginas(-10) # Intentando actualizar con un valor inválido