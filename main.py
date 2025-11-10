from libros import LibroFísico, LibroProtocol
from biblioteca import Biblioteca
from usuarios import SolicitanteLibro, Estudiante, Profesor, Familia
from exceptions import BibliotecaError

familia = Familia()
biblioteca = Biblioteca("Platzi biblioteca")

mi_libro = LibroFísico("100 años de soledad", "Gabriel Garcia M", "1234567890", True)
mi_libro_2 = LibroFísico("El fin de la eternidad", "Isaac Asimov", "1234567890", True)
mi_libro_3 = LibroFísico("Yo, robot", "Isaac Asimov", "1234567890", True)
mi_libro_4 = LibroFísico("El hombre bicentenario", "Isaac Asimov", "1234567890", True)

mi_libro_no_disponible = LibroFísico(
    "Fundación e imperio", "Isaac Asimov", "1234567890", False
)

lista_libros: list[LibroProtocol] = [
    mi_libro,
    mi_libro_2,
    mi_libro_3,
    mi_libro_4,
    mi_libro_no_disponible,
]


""" Implementaciones de usuarios """


def prestar_libros(solicitante: SolicitanteLibro, titulo, autor, isbn):
    solicitante.solicitar_libro(titulo, autor, isbn)
    return f"Libro {titulo} prestado con éxito"


estudiante = Estudiante("Pablo", "A1630637", "IMT")
profesor = Profesor("PabloT", "L157820528", "Ciencias e ingeniería")
profesor_2 = Profesor("Juanito", "L147820528", "Humanidades")
profesor_3 = Profesor("Rocio", "L15741828", "Ciencias e ingeniería")

usuarios_validos: list[SolicitanteLibro] = [
    estudiante,
    profesor,
    profesor_2,
    profesor_3,
]
try:
    prestar = mi_libro_no_disponible.prestar()
    print(prestar)
except BibliotecaError as e:
    print(f"Error: {e}, Tipo: {type(e)}")
#    print("Error, libro no se puede prestar")
# biblioteca.libros = lista_libros
# print(biblioteca.libros_disponibles())
try:
    result = estudiante.solicitar_libro("El título del libro", "El autor", None)
except BibliotecaError as e:
    print(f"Error: {e}, Tipo: {type(e)}")
    print("Error en la ejecución")
result = estudiante.solicitar_libro("El título del libro", "El autor", "2434NFRFNS")
print(result)


""" [
    print(prestar_libros(usuario, f"titulo_prueba_{i}", "autor_prueba", "isbn_prueba"))
    for i, usuario in enumerate[SolicitanteLibro](usuarios_validos)
] """
