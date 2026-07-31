from rich.console import Console
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
<<<<<<< HEAD
from rich.prompt import Prompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.rule import Rule
import time
from rich.align import Align
=======
from rich.prompt import Prompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.rule import Rule
import time
>>>>>>> 1dd32feda7e1d6c5d61e9ba225055581ebc501d5

console = Console()


<<<<<<< HEAD
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
        title="PYCHRONICLE UI",
        title_style="bold cyan",
        header_style="bold magenta"
        title="PYCHRONICLE MAIN MENU",
        title_style="bold cyan",
        header_style="bold magenta",
        show_header=True,
    )

    table.add_column("Key / Option", justify="center", style="green", width=15)
=======
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
>>>>>>> 1dd32feda7e1d6c5d61e9ba225055581ebc501d5
    table.add_column("Description", style="white")

    table.add_row("1", "Run Trace")
    table.add_row("2", "View Trace")
    table.add_row("3", "Replay Trace")
<<<<<<< HEAD
    table.add_row("4 or h", "Help Menu")
    table.add_row("5 or q", "Exit")
=======
    table.add_row("4", "Help")
    table.add_row("5", "Project Statistics")
    table.add_row("6", "About")
    table.add_row("7", "Exit")
>>>>>>> 1dd32feda7e1d6c5d61e9ba225055581ebc501d5

    console.print(table)

    console.print(
<<<<<<< HEAD
        "[bold blue]Tip:[/bold blue] Press [green]h[/green] for Help or "
        "[red]q[/red] to Exit.\n"
    )


=======
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
>>>>>>> 1dd32feda7e1d6c5d61e9ba225055581ebc501d5
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
<<<<<<< HEAD
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
=======
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
>>>>>>> 1dd32feda7e1d6c5d61e9ba225055581ebc501d5

    return True


<<<<<<< HEAD

# -------------------------
# Main Program
# -------------------------
def main():

    show_welcome()


    show_welcome()

    show_instructions()

=======
# -------------------------
# Main Program
# -------------------------
def main():

    show_welcome()

>>>>>>> 1dd32feda7e1d6c5d61e9ba225055581ebc501d5
    running = True

    while running:

<<<<<<< HEAD
=======
        console.print(Rule(style="cyan"))

>>>>>>> 1dd32feda7e1d6c5d61e9ba225055581ebc501d5

        console.print(Rule(style="cyan"))

        display_menu()


        choice = get_choice()

<<<<<<< HEAD
        running = process_choice(choice)
=======

        running = process_choice(choice)


if __name__ == "__main__":
    main()
>>>>>>> 1dd32feda7e1d6c5d61e9ba225055581ebc501d5



if __name__ == "__main__":
    main()