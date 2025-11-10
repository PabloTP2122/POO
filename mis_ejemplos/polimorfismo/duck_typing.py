from typing import Protocol


class Cerrable(Protocol):
    def close(self): ...


class Archivo:
    def close(self) -> str:
        return "Cerrando el archivo"


class ConexionRed:
    def close(self) -> str:
        return "Cerrando conexión a red"


class Perro:
    def ladrar(self):
        return "Guau, Guau"


def cerrar_recurso(recurso: Cerrable):
    print("Cerrando recurso...")
    recurso.close()


mi_archivo = Archivo()
mi_conexion = ConexionRed()

cerrar_recurso(mi_archivo)
cerrar_recurso(mi_conexion)

perro = Perro()
# cerrar_recurso(perro)
