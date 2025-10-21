class Libro:
    """Clase para representar un libro de una biblioteca"""

    # Constante de clase
    UMBRAL_POPULARIDAD = 5

    def __init__(
        self,
        titulo: str,
        autor: str,
        ISBN: str,
        disponible: bool = True,  # Valor por defecto
    ):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.disponible = disponible
        self.veces_prestado: int = 0

    def __str__(self) -> str:
        """Representación 'amigable' para el usuario final."""
        return f"Libro {self.titulo} por {self.autor} disponible: {self.disponible}"

    def __repr__(self):
        """Representación 'oficial' e inequívoca para desarrolladores."""
        return (
            f"Libro(titulo='{self.titulo}', autor='{self.autor}', "
            f"ISBN='{self.ISBN}', disponible={self.disponible}, "
            f"veces_prestado={self.veces_prestado})"
        )

    def prestar(self):
        """Presta el libro si está disponible."""
        if self.disponible:
            self.disponible = False

        self.veces_prestado += 1
        return True

    def devolver(self):
        """Devuelve el libro si estaba prestado."""
        # No se puede devolver un libro que ya está disponible.
        if self.disponible:
            return False
        self.disponible = True
        return True

    def es_popular(self):
        """Indica si el libro ha superado el umbral de popularidad."""
        return self.veces_prestado >= self.UMBRAL_POPULARIDAD


mi_libro = Libro("100 años de soledad", "Gabriel Garcia M", "1234567890", True)
mi_libro_2 = Libro("Fundación", "Isaac Asimov", "1234567890", True)


libros: list[Libro] = [
    mi_libro,
    Libro("El principito", "Saint-Exupéry", "1234567890", True),
    Libro("Fundación", "Isaac Asimov", "1234567890", True),
]

""" for i, libro in enumerate(libros):
    libro.print_book_info(i=i + 1) """

Libro.UMBRAL_POPULARIDAD = 5

for _ in range(5):
    print(mi_libro.prestar())
    print(mi_libro.devolver())

for _ in range(2):
    print(mi_libro_2.prestar())
    print(mi_libro_2.devolver())


# [libro.print_book_info(i=i + 1) for i, libro in enumerate(libros)]
# [print(libro) for libro in libros]
print(f"Libro: {mi_libro.titulo} , es Popular: ", mi_libro.es_popular())
print(f"Libro: {mi_libro_2.titulo} , es Popular: ", mi_libro_2.es_popular())
print(repr(mi_libro))
