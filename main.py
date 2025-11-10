from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

from biblioteca import Biblioteca
from exceptions import UsuarioNoEncontradoError
from libros import LibroFísico, LibroProtocol
from usuarios import Estudiante, Familia, Profesor, SolicitanteLibro

familia = Familia()
biblioteca = Biblioteca("Platzi biblioteca")

mi_libro = LibroFísico("100 años de soledad", "Gabriel Garcia M", "1234567890")
mi_libro_2 = LibroFísico("El fin de la eternidad", "Isaac Asimov", "1234567890")
mi_libro_3 = LibroFísico("Yo, robot", "Isaac Asimov", "1234567890")
mi_libro_4 = LibroFísico("El hombre bicentenario", "Isaac Asimov", "1234567890")
mi_libro_5 = LibroFísico("Fundación e imperio", "Isaac Asimov", "1234567890")
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

lista_libros: list[LibroProtocol] = [
    mi_libro,
    mi_libro_2,
    mi_libro_3,
    mi_libro_4,
    mi_libro_5,
]

biblioteca.usuarios = usuarios_validos
biblioteca.libros = lista_libros


console = Console()
# 1. Construye el contenido como un objeto Text (o un simple string)
contenido = Text()
contenido.append("Bienvenido a la Biblioteca de Platzi\n", style="bold green")
contenido.append("----------------------------\n", style="dim green")
contenido.append("Libros disponibles:\n", style="bold cyan")

for libro in biblioteca.libros_disponibles():
    # Añadimos viñetas para un look más limpio
    contenido.append(f"  • Título: {libro}\n", style="cyan")

# 2. Imprime UN SOLO Panel con ese contenido
console.print(
    Panel(
        contenido,
        title="[bold green]Mi Biblioteca creada en Platzi[/bold green]",
        border_style="green",
        padding=(1, 2),  # 1 línea arriba/abajo, 2 espacios izq/der
    )
)

cedula = Prompt.ask("[bold green]Digite el número de cédula[/bold green]")
try:
    usuario = biblioteca.buscar_usuario(cedula)
    print(Panel(f"Bienvenido: {usuario.nombre}", border_style="blue"))
except UsuarioNoEncontradoError as e:
    print(
        Panel(
            f"[bold red]Error:[/bold red] {e} \n [bold red]Tipo:[/bold red] {type(e)}",
            border_style="red",
        )
    )
