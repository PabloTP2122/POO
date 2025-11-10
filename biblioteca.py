from exceptions import UsuarioNoEncontradoError


class Biblioteca:
    def __init__(self, name):
        self.name = name
        # La composición se usa cuando un objeto está compuesto de otros objetos, o los "posee".
        # En este caso posee libros y usuarios
        self.libros = []
        self.usuarios = []

    def libros_disponibles(self) -> list:
        """Retorna el título del libro si está disponible"""
        return [libro.titulo for libro in self.libros if libro.disponible]

    def buscar_usuario(self, cedula):
        for usuario in self.usuarios:
            if usuario.cedula == cedula:
                return usuario
        raise UsuarioNoEncontradoError(
            f"El usuario con la cedula, {cedula} no se ha encontrado"
        )
