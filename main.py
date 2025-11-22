import sys
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

# Asumo que estas importaciones funcionan en tu entorno local
from exceptions import (
    LibroNoDisponibleError,
    LibroPrestadoError,
    UsuarioNoEncontradoError,
)
from helper_functions import print_errors
from persistencia import Persistencia


def mostrar_bienvenida(biblioteca, console):
    """Muestra la cabecera y los libros disponibles."""
    contenido = Text()
    contenido.append("Bienvenido a la Biblioteca de Platzi\n", style="bold green")
    contenido.append("-" * 36 + "\n", style="dim green")
    contenido.append("Libros disponibles:\n", style="bold cyan")

    for libro in biblioteca.libros_disponibles:
        contenido.append(f"  • Título: {libro.descripcion_completa}\n", style="cyan")

    console.print(
        Panel(
            contenido,
            title="[bold green]Mi Biblioteca creada en Platzi[/bold green]",
            border_style="green",
            padding=(1, 2),
        )
    )


def obtener_usuario(biblioteca):
    """
    Intenta obtener un usuario.
    Retorna el objeto usuario o None si el usuario decide salir/falla muchas veces.
    """
    while True:
        cedula = Prompt.ask(
            "[bold green]Digite el número de cédula (o 'salir' para cancelar)[/bold green]"
        )

        if cedula.lower() == "salir":
            return None

        try:
            usuario = biblioteca.buscar_usuario(cedula)
            print(Panel(f"¡Bienvenido {usuario.nombre}!", border_style="blue"))
            return usuario
        except UsuarioNoEncontradoError as e:
            print_errors(e)
            print("[yellow]Intente nuevamente.[/yellow]")


def obtener_libro(biblioteca):
    """Intenta obtener un libro válido."""
    while True:
        titulo = Prompt.ask(
            "[bold green]Digite el título del libro (o 'salir')[/bold green]"
        )

        if titulo.lower() == "salir":
            return None

        try:
            libro = biblioteca.buscar_libro(titulo)
            # Verificamos disponibilidad ANTES de retornar
            if not libro.disponible:
                raise LibroNoDisponibleError(f"El libro '{titulo}' no está disponible.")

            print(
                Panel(f"El libro seleccionado es: {libro.titulo}", border_style="green")
            )
            return libro
        except (LibroNoDisponibleError, Exception) as e:
            # Nota: Asumo que buscar_libro lanza error si no existe,
            # o agregamos lógica para LibroNoEncontrado.
            print_errors(e)


def main():
    persistencia = Persistencia()
    biblioteca = persistencia.cargar_datos()
    console = Console()

    mostrar_bienvenida(biblioteca, console)

    # 1. Paso Crítico: Obtener Usuario
    # Resolvemos el TODO: Si no hay usuario, no avanzamos.
    usuario = obtener_usuario(biblioteca)
    if not usuario:
        print("[bold red]Operación cancelada. Adiós.[/bold red]")
        return  # Salimos de la función main, terminando el programa

    # 2. Paso Crítico: Obtener Libro
    libro = obtener_libro(biblioteca)
    if not libro:
        print("[bold red]Operación cancelada. Adiós.[/bold red]")
        return

    # 3. Realizar el Préstamo
    # Aquí ya tenemos la certeza de que 'usuario' y 'libro' existen y son válidos.
    try:
        # Sugerencia POO: El método prestar debería ser atómico.
        # O el usuario pide el libro, o el libro se presta a un usuario.
        # Evita depender de strings para lógica de control.

        resultado_prestamo = (
            libro.prestar()
        )  # Asumiendo que esto actualiza el estado interno

        # Registramos que el usuario tiene el libro (si tu lógica lo requiere)
        usuario.solicitar_libro(libro.titulo)

        console.print(
            Panel(
                Text(f"Éxito: {resultado_prestamo}", style="bold blue"),
                title="[bold green]Préstamo Finalizado[/bold green]",
                border_style="green",
                padding=(1, 2),
            )
        )

        # Guardamos cambios solo si todo salió bien
        persistencia.guardar_datos(biblioteca)

    except (LibroPrestadoError, LibroNoDisponibleError) as e:
        print_errors(e)
    except Exception as e:
        print(f"[bold red]Error inesperado: {e}[/bold red]")


if __name__ == "__main__":
    main()
