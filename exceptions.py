# Agrupa las excepciones de la biblioteca
class BibliotecaError(Exception):
    """Excepción base para errores de la biblioteca"""

    pass


# Esta excepción está dentro de biblioteca, así que puede ser
# fácilmente capturada por un bloque try-except
class DatosLibroInvalidError(BibliotecaError):
    """Datos de libro no son correctos o son inválidos"""

    pass


class LibroNoDisponibleError(BibliotecaError):
    """El libro solicitado no está disponible para préstamo"""

    pass
