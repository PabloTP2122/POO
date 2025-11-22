from abc import ABC, abstractmethod
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


class LibroBase(ABC):
    """Métodos que todo Libro debe tener"""

    @abstractmethod
    def prestar(self):
        """Método para prestar libro"""
        ...

    @abstractmethod
    def devolver(self):
        """Método usado para devolver libro"""
        ...

    @abstractmethod
    def calcular_duracion(self):
        """Método para calcular la duración del prestamo"""
        ...


class Libro(LibroBase):
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

    # Método que permite crear una variación del constructor de la clase
    # Crea un método constructor
    @classmethod
    def crear_no_sisponible(
        cls,
        titulo: str,
        autor: str,
        ISBN: str,
    ):
        return cls(
            titulo,
            autor,
            ISBN,
            disponible=False,
        )

    def prestar(self) -> str:
        """Presta el libro si está disponible. Devuelve True si fue exitoso."""
        if not self.disponible:
            raise LibroNoDisponibleError(
                f"El libro solicitado: {self.titulo}, no está disponible"
            )
        if self.disponible:
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

    @property
    def es_popular(self) -> bool:
        """Indica si el libro ha superado el umbral de popularidad."""
        return self.__veces_prestado >= self.UMBRAL_POPULARIDAD

    @property
    def veces_prestado(self) -> int:
        return self.__veces_prestado

    @veces_prestado.setter
    def veces_prestado(self, veces_prestado):
        if veces_prestado > 0:
            self.__veces_prestado = veces_prestado
        raise ValueError("El vlaor de veces_prestado, debe ser mayor a cero")

    @property
    def descripcion_completa(self):
        return f"{self.titulo} por {self.autor}, ISBN: {self.ISBN}"


class LibroFísico(Libro):
    def calcular_duracion(self):
        return "7 días"


class LibroDigital(Libro):
    def calcular_duracion(self):
        return "14 días"
