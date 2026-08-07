from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, Confirm, IntPrompt
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.rule import Rule
import time

console = Console()


def show_title():
    console.print(
        Panel.fit(
            "[bold cyan]PyChronicle[/bold cyan]\n"
            "[white]Execution Trace System[/white]",
            border_style="cyan",
            padding=(1, 6),
        )
    )


def show_menu():
    table = Table(
        title="[bold cyan]Main Menu[/bold cyan]",
        show_header=True,
        header_style="bold magenta",
    )

    table.add_column("Option", justify="center", style="green", width=10)
    table.add_column("Feature", style="yellow", width=30)

    table.add_row("1", "View Runs")
    table.add_row("2", "Replay Trace")
    table.add_row("3", "Search Variable")
    table.add_row("4", "Execution Statistics")
    table.add_row("5", "Export JSON")
    table.add_row("6", "Delete Run")
    table.add_row("7", "Help")
    table.add_row("8", "About")
    table.add_row("9", "Run Details")
    table.add_row("10", "Compare Runs")
    table.add_row("11", "Compare Variables")
    table.add_row("12", "Execution Timeline")
    table.add_row("0", "Exit")

    console.print(table)


def get_menu_choice():
    while True:
        try:
            choice = IntPrompt.ask(
                "[bold cyan]Select an option[/bold cyan]",
                default=1,
            )

            if choice in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
                return choice

            show_error("Please choose a valid option.")

        except Exception:
            show_error("Invalid input. Enter a number.")


def show_success(message):
    console.print(f"[bold green]✓ {message}[/bold green]")


def show_error(message):
    console.print(f"[bold red]✗ {message}[/bold red]")


def show_warning(message):
    console.print(f"[bold yellow]! {message}[/bold yellow]")


def show_info(message):
    console.print(f"[bold cyan]{message}[/bold cyan]")


def show_message(message, style="green"):
    console.print(f"[{style}]{message}[/{style}]")


def loading(message="Loading..."):
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description=message, total=None)
        time.sleep(2)


def confirm_exit():
    return Confirm.ask(
        "[bold red]Are you sure you want to exit?[/bold red]"
    )


def show_help():
    console.print(
        Panel(
            """[bold cyan]PyChronicle Help[/bold cyan]

1 → View all execution runs
2 → Replay execution trace
3 → Search variable history
4 → View execution statistics
5 → Export trace to JSON
6 → Delete an execution run
7 → View Help
8 → About PyChronicle
9 → View details of a specific run
10 → Compare execution runs
11 → Compare variables
12 → View execution timeline
0 → Exit application
""",
            title="User Guide",
            border_style="green",
        )
    )


def show_about():
    console.print(
        Panel.fit(
            """[bold cyan]PyChronicle[/bold cyan]

Execution Trace System

Version : 1.0

Features
• Execution tracing
• Variable history
• Replay execution
• JSON export
• Statistics
• Delete execution history
• Run details
• Compare runs

Developed using Python + SQLite + Rich
""",
            border_style="blue",
        )
    )


def divider():
    console.print(Rule(style="cyan"))


def pause():
    Prompt.ask("\nPress Enter to continue")