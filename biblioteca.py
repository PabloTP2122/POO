from exceptions import UsuarioNoEncontradoError, LibroNoDisponibleError


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        # La composición se usa cuando un objeto está compuesto de otros objetos, o los "posee".
        # En este caso posee libros y usuarios
        self.libros = []
        self.usuarios = []

    @property
    def libros_disponibles(self) -> list:
        """Retorna el título del libro si está disponible"""
        return [libro for libro in self.libros if libro.disponible]

    def buscar_usuario(self, cedula):
        """Permite buscar entre los usuarios disponibles"""
        for usuario in self.usuarios:
            if usuario.cedula == cedula:
                return usuario
        raise UsuarioNoEncontradoError(
            f"El usuario con la cedula, {cedula} no se ha encontrado"
        )

    def buscar_libro(self, titulo):
        """Permite la búsqueda de un libro dentro de la biblioteca"""
        for libro in self.libros:
            if libro.titulo == titulo and libro.disponible:
                return libro
        raise LibroNoDisponibleError(
            f"El libro con título '{titulo}', no está en la biblioteca o no existe"
        )

    # Static method
    # No recibe self, porque no necesita una instancia
    @staticmethod
    def validar_isbn(isbn: str):
        return len(isbn) >= 10
