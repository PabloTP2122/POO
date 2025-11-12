from libros import LibroDigital, LibroProtocol, LibroFísico
from usuarios import Estudiante, Profesor, SolicitanteLibro


# Create 10 Libros físicos
mi_libro = LibroFísico("100 años de soledad", "Gabriel Garcia M", "1234567890")
mi_libro_2 = LibroFísico("El fin de la eternidad", "Isaac Asimov", "1234567890")
mi_libro_3 = LibroFísico("Yo, robot", "Isaac Asimov", "1234567890")
mi_libro_4 = LibroFísico("El hombre bicentenario", "Isaac Asimov", "1234567890")
mi_libro_5 = LibroFísico("Fundación e imperio", "Isaac Asimov", "1234567890")
mi_libro_6 = LibroFísico("El juego de Ender", "Orson Scott Card", "1234567890")
mi_libro_7 = LibroFísico(
    "El misterio de la pirámide", "Arthur Conan Doyle", "1234567890"
)
mi_libro_8 = LibroFísico("El alquimista", "Paulo Coelho", "1234567890")
mi_libro_9 = LibroFísico("El principito", "Antoine de Saint-Exupéry", "1234567890")
mi_libro_10 = LibroFísico("El arte de la guerra", "Sun Tzu", "1234567890")


# Create 10 Libros digitales
mi_libro_digital_1 = LibroDigital(
    "100 años de soledad", "Gabriel Garcia M", "1234567890"
)
mi_libro_digital_2 = LibroDigital(
    "El fin de la eternidad", "Isaac Asimov", "1234567890"
)
mi_libro_digital_3 = LibroDigital("Yo, robot", "Isaac Asimov", "1234567890")
mi_libro_digital_4 = LibroDigital(
    "El hombre bicentenario", "Isaac Asimov", "1234567890"
)
mi_libro_digital_5 = LibroDigital("Fundación e imperio", "Isaac Asimov", "1234567890")
mi_libro_digital_6 = LibroDigital("El juego de Ender", "Orson Scott Card", "1234567890")
mi_libro_digital_7 = LibroDigital(
    "El misterio de la pirámide", "Arthur Conan Doyle", "1234567890"
)
mi_libro_digital_8 = LibroDigital("El alquimista", "Paulo Coelho", "1234567890")
mi_libro_digital_9 = LibroDigital(
    "El principito", "Antoine de Saint-Exupéry", "1234567890"
)
mi_libro_digital_10 = LibroDigital("El arte de la guerra", "Sun Tzu", "1234567890")


# Create 10 Students
mi_estudiante_1 = Estudiante("Pablo", "A1630637", "IMT")
mi_estudiante_2 = Estudiante("Juan", "A1645637", "IMT")
mi_estudiante_3 = Estudiante("Maria", "A1656637", "IMT")
mi_estudiante_4 = Estudiante("Pedro", "A1667637", "IMT")
mi_estudiante_5 = Estudiante("Ana", "A1678637", "IMT")
mi_estudiante_6 = Estudiante("Luis", "A1689637", "IMT")
mi_estudiante_7 = Estudiante("Carlos", "A1690637", "IMT")
mi_estudiante_8 = Estudiante("Ana", "A1601637", "IMT")
mi_estudiante_9 = Estudiante("Luis", "A1612637", "IMT")
mi_estudiante_10 = Estudiante("Carlos", "A1623637", "IMT")


# Otros usuarios validos
profesor = Profesor("Pablo TP (Profesor)", "L157820528", "Ciencias e ingeniería")
profesor_2 = Profesor("Juanito (Profesor)", "L147820528", "Humanidades")
profesor_3 = Profesor("Rocio (Profesor)", "L15741828", "Ciencias e ingeniería")

usuarios_validos: list[SolicitanteLibro] = [
    profesor,
    profesor_2,
    profesor_3,
]

# Otros libros
mi_libro_custom = LibroFísico("100 años de soledad", "Gabriel Garcia M", "1234567890")
mi_libro_custom_2 = LibroFísico("El fin de la eternidad", "Isaac Asimov", "1234567890")
mi_libro_custom_3 = LibroFísico("Yo, robot", "Isaac Asimov", "1234567890")
mi_libro_custom_4 = LibroFísico("El hombre bicentenario", "Isaac Asimov", "1234567890")
mi_libro_custom_5 = LibroFísico("Fundación e imperio", "Isaac Asimov", "1234567890")

lista_libros_custom: list[LibroProtocol] = [
    mi_libro_custom,
    mi_libro_custom_2,
    mi_libro_custom_3,
    mi_libro_custom_4,
    mi_libro_custom_5,
]

lista_libros = [
    mi_libro,
    mi_libro_2,
    mi_libro_3,
    mi_libro_4,
    mi_libro_5,
    mi_libro_6,
    mi_libro_7,
    mi_libro_8,
    mi_libro_9,
    mi_libro_10,
]

lista_libros_digitales = [
    mi_libro_digital_1,
    mi_libro_digital_2,
    mi_libro_digital_3,
    mi_libro_digital_4,
    mi_libro_digital_5,
    mi_libro_digital_6,
    mi_libro_digital_7,
    mi_libro_digital_8,
    mi_libro_digital_9,
    mi_libro_digital_10,
]

lista_estudiantes = [
    mi_estudiante_1,
    mi_estudiante_2,
    mi_estudiante_3,
    mi_estudiante_4,
    mi_estudiante_5,
    mi_estudiante_6,
    mi_estudiante_7,
    mi_estudiante_8,
    mi_estudiante_9,
    mi_estudiante_10,
]
