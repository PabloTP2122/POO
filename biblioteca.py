class Biblioteca:
    def __init__(self, name):
        self.name = name
        # La composición se usa cuando un objeto está compuesto de otros objetos, o los "posee".
        # En este caso posee libros y usuarios
        self.libros = []
        self.usuarios = []

    def libros_disponibles(self) -> list:
        return [libro.titulo for libro in self.libros if libro.disponible]
