import json
from datetime import datetime
from biblioteca import Biblioteca
from libros import LibroFísico
from usuarios import Estudiante, Profesor


class Persistencia:
    def __init__(self, archivo: str = "biblioteca.json") -> None:
        self.archivo = archivo

    def guardar_datos(self, biblioteca):
        datos = {
            "nombre": biblioteca.nombre,
            "usuarios": [usuario.__dict__ for usuario in biblioteca.usuarios],
            "libros": [libro.__dict__ for libro in biblioteca.libros],
            "fecha_guardado": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        }
        # Context manager para utilizar archivo
        # de forma apropiada
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

    def cargar_datos(self):
        # 1. Leer el archivo que ya está creado en el directorio raiz
        with open(self.archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
        # 2. Retornar el objeto con la información del archivo
        # 2.1 Requiere volver a reconstruir el archivo
        biblioteca = Biblioteca(datos["nombre"])
        for dato_libro in datos["libros"]:
            libro = LibroFísico(
                titulo=dato_libro["titulo"],
                autor=dato_libro["autor"],
                ISBN=dato_libro["ISBN"],
                disponible=dato_libro["disponible"],
            )
            biblioteca.libros.append(libro)

        for dato_usuario in datos["usuarios"]:
            # TODO: mejorar agregando al objeto usuario el
            # tipo de usuario (Profesor/Estudiante)
            if "carrera" in dato_usuario:
                usuario = Estudiante(
                    nombre=dato_usuario["nombre"],
                    cedula=dato_usuario["cedula"],
                    carrera=dato_usuario["carrera"],
                )
            else:
                usuario = Profesor(
                    nombre=dato_usuario["nombre"],
                    cedula=dato_usuario["cedula"],
                    departamento=dato_usuario["departamento"],
                )

            biblioteca.usuarios.append(usuario)
        return biblioteca
