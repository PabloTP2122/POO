from rich import print
from rich.panel import Panel


def print_errors(e):
    print(
        Panel(
            f"[bold red]Error:[/bold red] {e} \n [bold red]Tipo:[/bold red] {type(e)}",
            border_style="red",
        )
    )
