from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.rule import Rule
import time

console = Console()


# -------------------------
# Welcome Screen
# -------------------------
def show_welcome():
    console.print(
        Panel.fit(
            "[bold cyan]PyChronicle[/bold cyan]\n"
            "[green]Execution Trace System[/green]",
            border_style="cyan",
            padding=(1, 6),
        )
    )


# -------------------------
# Main Menu
# -------------------------
def display_menu():

    table = Table(
        title="PYCHRONICLE MAIN MENU",
        title_style="bold cyan",
        header_style="bold magenta",
        show_header=True,
    )

    table.add_column("Option", justify="center", style="green", width=12)
    table.add_column("Description", style="white")

    table.add_row("1", "Run Trace")
    table.add_row("2", "View Trace")
    table.add_row("3", "Replay Trace")
    table.add_row("4", "Help")
    table.add_row("5", "Project Statistics")
    table.add_row("6", "About")
    table.add_row("7", "Exit")

    console.print(table)

    console.print(
        "[dim]Shortcut Keys : h = Help | q = Exit[/dim]",
        justify="center",
    )


# -------------------------
# Loading Animation
# -------------------------
def loading(text):

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}")
    ) as progress:

        progress.add_task(description=text, total=None)
        time.sleep(1.5)


# -------------------------
# Messages
# -------------------------
def success(msg):
    console.print(f"[bold green]✓ {msg}[/bold green]")


def error(msg):
    console.print(f"[bold red]✗ {msg}[/bold red]")


def warning(msg):
    console.print(f"[bold yellow]! {msg}[/bold yellow]")


# -------------------------
# User Choice
# -------------------------
def get_choice():

    shortcuts = {
        "h": 4,
        "q": 7
    }

    while True:

        user = Prompt.ask(
            "\n[bold cyan]Enter option[/bold cyan]"
        ).strip().lower()

        if user == "":
            error("Input cannot be empty.")
            continue

        if user in shortcuts:
            return shortcuts[user]

        if user.isdigit():

            choice = int(user)

            if 1 <= choice <= 7:
                return choice

            error("Choose between 1 and 7.")

        else:

            error("Invalid input.")


# -------------------------
# Help Screen
# -------------------------
def help_menu():

    console.print(
        Panel(
            """
[bold cyan]Help Menu[/bold cyan]

1 → Run Trace
2 → View Trace
3 → Replay Trace
4 → Help
5 → Project Statistics
6 → About
7 → Exit

Keyboard Shortcuts

h → Help
q → Quit
""",
            title="Help",
            border_style="blue",
        )
    )


# -------------------------
# Statistics
# -------------------------
def statistics():

    table = Table(title="Project Statistics")

    table.add_column("Module", style="green")
    table.add_column("Status", style="cyan")

    table.add_row("Trace Engine", "Available")
    table.add_row("Replay", "Available")
    table.add_row("Viewer", "Available")
    table.add_row("Export", "JSON")
    table.add_row("Database", "SQLite")
    table.add_row("Rich UI", "Enabled")

    console.print(table)


# -------------------------
# About
# -------------------------
def about():

    console.print(
        Panel.fit(
            """
[bold cyan]PyChronicle[/bold cyan]

Execution Trace System

Version : 1.0

Developed using

• Python
• Rich Library
• SQLite
""",
            title="About",
            border_style="green",
        )
    )


# -------------------------
# Choice Handler
# -------------------------
def process_choice(choice):

    console.print()

    if choice == 1:

        loading("Running Trace...")
        success("Trace completed successfully.")

    elif choice == 2:

        loading("Opening Trace Viewer...")
        success("Viewer opened.")

    elif choice == 3:

        loading("Replaying Trace...")
        success("Replay completed.")

    elif choice == 4:

        help_menu()

    elif choice == 5:

        statistics()

    elif choice == 6:

        about()

    elif choice == 7:

        if Confirm.ask(
            "[bold red]Are you sure you want to exit?[/bold red]"
        ):

            success("Thank you for using PyChronicle.")
            return False

        warning("Returning to menu.")

    return True


# -------------------------
# Main Program
# -------------------------
def main():

    show_welcome()

    running = True

    while running:

        console.print(Rule(style="cyan"))

        display_menu()

        choice = get_choice()

        running = process_choice(choice)


if __name__ == "__main__":
    main()