from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

from biblioteca import Biblioteca
from data import lista_estudiantes, lista_libros, usuarios_validos
from exceptions import LibroNoDisponibleError, UsuarioNoEncontradoError
from helper_functions import print_errors


biblioteca = Biblioteca("Platzi biblioteca")
biblioteca.usuarios = lista_estudiantes + usuarios_validos
biblioteca.libros = lista_libros


console = Console()
# 1. Construye el contenido como un objeto Text (o un simple string)
contenido = Text()
contenido.append("Bienvenido a la Biblioteca de Platzi\n", style="bold green")
contenido.append("------------------------------------\n", style="dim green")
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
    print(Panel(f"¡Bienvenido {usuario.nombre}!", border_style="blue"))
except UsuarioNoEncontradoError as e:
    print_errors(e)

titulo = Prompt.ask("[bold green]Digite el título del libro[/bold green]")
try:
    libro = biblioteca.buscar_libro(titulo)
    print(Panel(f"El libro seleccionado es: {titulo}", border_style="green"))
except LibroNoDisponibleError as e:
    print_errors(e)

resultado_final = Text()
console_2 = Console()
resultado = str(usuario.solicitar_libro(libro.titulo))
resultado_final.append(resultado, style="bold blue")

try:
    resultado_prestar: str = str(libro.prestar())
    resultado_final.append("\n")
    resultado_final.append(resultado_prestar, style="bold blue")
    console_2.print(
        Panel(
            resultado_final,
            title="[bold green]Préstamo[/bold green]",
            border_style="green",
            padding=(1, 2),  # 1 línea arriba/abajo, 2 espacios izq/der)
        )
    )
except LibroNoDisponibleError as e:
    print_errors(e)
