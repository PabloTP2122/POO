from libros import Libro
from typing import Protocol
from exceptions import DatosLibroInvalidError


class SolicitanteLibro(Protocol):
    """Método que debe implementar cualquier solicitante"""

    def solicitar_libro(self, titulo: str, autor: str, isbn: str) -> str: ...


class Usuario:
    def __init__(self, nombre: str, cedula: str):
        self.nombre = nombre
        self.cedula = cedula
        self.libros_prestados: list[Libro] = []

    def solicitar_libro(self, titulo, autor, isbn) -> str:
        return f"Solicitud del libro realizada {titulo}"


class Estudiante(Usuario):
    def __init__(self, nombre: str, cedula: str, carrera: str, limite_libros: int = 3):
        super().__init__(nombre, cedula)
        self.carrera = carrera
        self.limite_libros = 3

    def solicitar_libro(self, titulo: str, autor: str, isbn: str) -> str:
        if not titulo or not autor or not isbn:
            raise DatosLibroInvalidError(
                f"Ninguno de los datos del libro puede estar vacío: {titulo}, {autor}, {isbn}"
            )
        if len(self.libros_prestados) < self.limite_libros:
            self.libros_prestados.append(Libro(titulo, autor, isbn))
            return f"Libro con título {titulo} correctamente prestado"
        return f"Límite de préstamos alcanzado, límite: {self.limite_libros}"


class Profesor(Usuario):
    def __init__(self, nombre: str, cedula: str, departamento: str):
        super().__init__(nombre, cedula)
        self.departamento = departamento
        self.limite_libros = None


# Ejemplo que no implementa el método solicitar_libro
class Familia:
    def un_metodo(self): ...
