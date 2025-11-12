from typing import Protocol
from exceptions import LibroNoDisponibleError


class LibroProtocol(Protocol):
    """Métodos que todo Libro debe tener"""

    def prestar(self):
        """Método para prestar libro"""
        ...

    def devolver(self):
        """Método usado para devolver libro"""
        ...

    def calcular_duracion(self):
        """Método para calcular la duración del prestamo"""
        ...


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
        self.__veces_prestado: int = 0

    def __str__(self) -> str:
        """Representación 'amigable' para el usuario final."""
        return f"Libro {self.titulo} por {self.autor} disponible: {self.disponible}"

    def __repr__(self):
        """Representación 'oficial' e inequívoca para desarrolladores."""
        return (
            f"Libro(titulo='{self.titulo}', autor='{self.autor}', "
            f"ISBN='{self.ISBN}', disponible={self.disponible}, "
            f"veces_prestado={self.__veces_prestado})"
        )

    def prestar(self) -> str:
        """Presta el libro si está disponible. Devuelve True si fue exitoso."""
        if not self.disponible:
            raise LibroNoDisponibleError(
                f"El libro solicitado: {self.titulo}, no está disponible"
            )

        self.disponible = False
        self.__veces_prestado += 1
        return f"'{self.titulo}' prestado exitosamente. Total prestamos: {self.__veces_prestado}"

    def calcular_duracion(self):
        """Calcula la duración de un préstamo"""
        ...

    def devolver(self):
        """Devuelve el libro si estaba prestado."""
        # No se puede devolver un libro que ya está disponible.
        if self.disponible:
            return False
        self.disponible = True
        return True

    def es_popular(self) -> bool:
        """Indica si el libro ha superado el umbral de popularidad."""
        return self.__veces_prestado >= self.UMBRAL_POPULARIDAD

    def get_veces_prestado(self) -> int:
        return self.__veces_prestado

    def set_veces_prestado(self, veces_prestado):
        self.__veces_prestado = veces_prestado


class LibroFísico(Libro):
    def calcular_duracion(self):
        return "7 días"


class LibroDigital(Libro):
    def calcular_duracion(self):
        return "14 días"
