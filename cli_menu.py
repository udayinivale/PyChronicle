from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.rule import Rule
from rich.align import Align
import time

console = Console()


def show_welcome():
    console.print(
        Panel.fit(
            "[bold cyan]Welcome to PyChronicle[/bold cyan]\n\n"
            "PyChronicle helps you manage execution traces.\n"
            "Follow the instructions below to use the application.",
            border_style="cyan",
            title="WELCOME"
        )
    )


def show_instructions():
    console.print(
        Panel(
            "[bold yellow]Instructions[/bold yellow]\n\n"
            "• Enter numbers [green]1 - 5[/green] to select a menu option.\n"
            "• Press [bold green]'h'[/bold green] anytime to open Help.\n"
            "• Press [bold red]'q'[/bold red] anytime to Exit.\n"
            "• Empty or invalid inputs are not accepted.\n"
            "• Follow the prompts displayed on the screen.",
            border_style="yellow",
            title="USER GUIDE"
        )
    )


def display_menu():


    table = Table(
    title="PYCHRONICLE MAIN MENU",
    title_style="bold cyan",
    header_style="bold magenta",
    show_header=True
)

    table.add_column("Key / Option", justify="center", style="green", width=15)
    table.add_column("Description", style="white")

    table.add_row("1", "Run Trace")
    table.add_row("2", "View Trace")
    table.add_row("3", "Replay Trace")
    table.add_row("4 or h", "Help Menu")
    table.add_row("5 or q", "Exit")

    console.print(table)

    console.print(
        "[bold blue]Tip:[/bold blue] Press [green]h[/green] for Help or "
        "[red]q[/red] to Exit.\n"
    )


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
        "q": 5
    }

    while True:

        user = Prompt.ask(
            "\n[bold cyan]Enter option[/bold cyan]"
        ).strip().lower()

        user_input = input("Select option (1-5, h, q): ").strip().lower()

        if user == "":
            error("Input cannot be empty.")
        if user_input == "":
            print("[bold red]Input cannot be empty.[/bold red]")
            continue

        if user_input in shortcuts:
            return shortcuts[user_input]

        if user_input.isdigit():

            choice = int(user_input)

            if 1 <= choice <= 5:
                return choice

            print("[bold red]Please enter numbers between 1 and 5.[/bold red]")
            continue

        console.print(
            Panel(
                "[red]Invalid Choice![/red]\n\n"
                "Valid Inputs:\n"
                "1\n2\n3\n4 (or h)\n5 (or q)",
                title="INPUT GUIDE",
                border_style="red"
            )
        )


def process_choice(choice):

    print()

    if choice == 1:

        console.print(
            Panel.fit(
                "[green]✓ Trace executed successfully.[/green]",
                border_style="green"
            )
        )

    elif choice == 2:

        console.print(
            Panel.fit(
                "[cyan]✓ Trace Viewer opened successfully.[/cyan]",
                border_style="cyan"
            )
        )

    elif choice == 3:

        console.print(
            Panel.fit(
                "[yellow]✓ Replay started successfully.[/yellow]",
                border_style="yellow"
            )
        )

    elif choice == 4:

        console.print(
            Panel(
                "[bold cyan]Help Menu[/bold cyan]\n\n"

                "[bold]Menu Options[/bold]\n"
                "1 → Run Trace\n"
                "2 → View Trace\n"
                "3 → Replay Trace\n"
                "4 → Help Menu\n"
                "5 → Exit Program\n\n"

                "[bold]Keyboard Shortcuts[/bold]\n"
                "h → Help\n"
                "q → Exit\n\n"

                "[bold]Tips[/bold]\n"
                "• Enter only numbers between 1 and 5.\n"
                "• Use shortcuts for quick access.\n"
                "• Follow on-screen instructions.",
                title="HELP",
                border_style="blue"
            )
        )

    elif choice == 5:

        confirm = input("Are you sure you want to exit? (y/n): ").strip().lower()

        if confirm == "y":

            console.print(
                Panel.fit(
                    Align.center(
                        "[bold green]Goodbye![/bold green]\n\n"
                        "Thank you for using\n"
                        "[bold cyan]PyChronicle[/bold cyan]\n\n"
                        "Have a productive day!"
                    ),
                    border_style="green",
                    title="EXIT"
                )
            )

            return False



        warning("Returning to menu.")

    return True



# -------------------------
# Main Program
# -------------------------
def main():

    show_welcome()


    show_welcome()

    show_instructions()

    running = True

    while running:


        console.print(Rule(style="cyan"))

        display_menu()


        choice = get_choice()

        running = process_choice(choice)



if __name__ == "__main__":
    main()