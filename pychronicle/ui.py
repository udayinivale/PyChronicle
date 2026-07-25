from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def show_title():
    console.print(
        Panel.fit(
            "[bold cyan]PyChronicle[/bold cyan]\nExecution Trace System",
            border_style="cyan"
        )
    )


def show_menu():
    table = Table(title="Main Menu")

    table.add_column("Option", style="green", justify="center")
    table.add_column("Description", style="yellow")

    table.add_row("1", "View Runs")
    table.add_row("2", "Replay Trace")
    table.add_row("3", "Export JSON")
    table.add_row("4", "Exit")

    console.print(table)


def show_message(message, style="green"):
    console.print(f"[{style}]{message}[/{style}]")