from typing import Protocol
from exceptions import DatosLibroInvalidError, LibroPrestadoError
from abc import ABC, abstractmethod


class SolicitanteLibro(Protocol):
    """Método que debe implementar cualquier solicitante"""

    def solicitar_libro(self, titulo: str) -> str: ...


class UsuarioBase(ABC):
    """Métodos que debe tener cualquier clase que se gnenere desde UsuarioBase"""

    @abstractmethod
    def solicitar_libro(self, titulo):
        pass


class Usuario(UsuarioBase):
    def __init__(self, nombre: str, cedula: str):
        self.nombre = nombre
        self.cedula = cedula
        self.libros_prestados: list[str] = []

    def solicitar_libro(self, titulo) -> str:
        return f"Solicitud del libro realizada {titulo}"

    @property
    def nombre_completo(self):
        return f"{self.nombre}, con cedula: {self.cedula}"


class Estudiante(Usuario):
    def __init__(self, nombre: str, cedula: str, carrera: str, limite_libros: int = 3):
        super().__init__(nombre, cedula)
        self.carrera = carrera
        self.limite_libros = 3

    @classmethod
    def estudiante_economia(cls, nombre: str, cedula: str):
        return cls(nombre, cedula, carrera="Economía")

    def solicitar_libro(self, titulo: str) -> str:
        if titulo in self.libros_prestados:
            raise LibroPrestadoError(
                f"El libro con título: {titulo}, ya fue prestado al usuario."
            )
        if not titulo:
            raise DatosLibroInvalidError(f"El título no debe estar vacío: {titulo}")
        if len(self.libros_prestados) < self.limite_libros:
            print(
                f"libros_prestados: {len(self.libros_prestados)}\n Libros: {self.libros_prestados}"
            )
            self.libros_prestados.append(titulo)
            return f"Libro con título: '{titulo}', correctamente prestado"
        else:
            return f"Límite de préstamos alcanzado, límite: {self.limite_libros}"


class Profesor(Usuario):
    def __init__(self, nombre: str, cedula: str, departamento: str):
        super().__init__(nombre, cedula)
        self.departamento = departamento
        self.limite_libros = None

    def solicitar_libro(self, titulo):
        self.libros_prestados.append(titulo)
        return f"Prestamo del libro: {titulo} autorizado"


# Ejemplo que no implementa el método solicitar_libro para explicar
# la composición
class Familia:
    def un_metodo(self): ...
