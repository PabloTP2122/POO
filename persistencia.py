import json
from datetime import datetime


class Persistencia:
    def __init__(self, archivo: str = "biblioteca.json") -> None:
        self.archivo = archivo

    def guardar_datos(self, biblioteca):
        datos = {
            "nombre": biblioteca.nombre,
            "usuarios": [usuario.__dict__ for usuario in biblioteca.usuarios],
            "libros": [libro.__dict__ for libro in biblioteca.libros],
            "fecha_guardado": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        # Context manager para utilizar archivo
        # de forma apropiada
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
