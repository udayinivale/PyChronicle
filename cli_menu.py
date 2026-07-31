from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.rule import Rule
from rich.align import Align
import time

console = Console()


# ==========================================
# WELCOME SCREEN
# ==========================================

def show_welcome():
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Welcome to PyChronicle[/bold cyan]\n\n"
            "[white]Python Code Execution Trace Management System[/white]\n\n"
            "[green]✔ Trace Python Programs\n"
            "✔ View Previous Traces\n"
            "✔ Replay Execution\n"
            "✔ Search Traces\n"
            "✔ Export Reports[/green]",
            title="[bold blue]WELCOME[/bold blue]",
            border_style="cyan"
        )
    )


# ==========================================
# USER GUIDE
# ==========================================

def show_instructions():

    console.print(
        Panel(
            "[bold yellow]Instructions[/bold yellow]\n\n"

            "1. Enter numbers between [green]1 - 8[/green].\n"
            "2. Press [green]h[/green] for Help.\n"
            "3. Press [red]q[/red] for Exit.\n"
            "4. Invalid inputs are rejected.\n"
            "5. Follow the on-screen instructions.",

            title="USER GUIDE",
            border_style="yellow"
        )
    )


# ==========================================
# LOADING ANIMATION
# ==========================================

def loading(text):

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}")
    ) as progress:

        progress.add_task(description=text, total=None)
        time.sleep(2)


# ==========================================
# MESSAGE FUNCTIONS
# ==========================================

def success(msg):
    console.print(f"[bold green]✔ {msg}[/bold green]")


def error(msg):
    console.print(f"[bold red]✘ {msg}[/bold red]")


def warning(msg):
    console.print(f"[bold yellow]⚠ {msg}[/bold yellow]")


# ==========================================
# MAIN MENU
# ==========================================

def display_menu():

    console.print(Rule("[bold cyan]PYCHRONICLE MAIN MENU[/bold cyan]"))

    table = Table(
        show_header=True,
        header_style="bold magenta",
        title="MAIN MENU",
        title_style="bold cyan"
    )

    table.add_column("Option", justify="center", style="green", width=12)
    table.add_column("Description", style="white")

    table.add_row("1", "Run Trace")
    table.add_row("2", "View Trace")
    table.add_row("3", "Replay Trace")
    table.add_row("4", "Search Trace")
    table.add_row("5", "Statistics")
    table.add_row("6", "Export Report")
    table.add_row("7 / h", "Help")
    table.add_row("8 / q", "Exit")

    console.print(table)

    console.print(
        "[bold blue]Tip:[/bold blue] "
        "Use [green]h[/green] for Help and "
        "[red]q[/red] to Exit.\n"
    )
# ==========================================
# USER INPUT
# ==========================================

def get_choice():

    shortcuts = {
        "h": 7,
        "q": 8
    }

    while True:

        user_input = Prompt.ask(
            "[bold cyan]Select option (1-8, h, q)[/bold cyan]"
        ).strip().lower()

        # Empty input
        if user_input == "":
            error("Input cannot be empty.")
            continue

        # Shortcut keys
        if user_input in shortcuts:
            return shortcuts[user_input]

        # Number validation
        if user_input.isdigit():

            choice = int(user_input)

            if 1 <= choice <= 8:
                return choice

            error("Please enter a number between 1 and 8.")
            continue

        # Invalid input guide
        console.print(
            Panel(
                "[bold red]Invalid Choice![/bold red]\n\n"
                "Valid Inputs:\n\n"
                "[green]1[/green]  Run Trace\n"
                "[green]2[/green]  View Trace\n"
                "[green]3[/green]  Replay Trace\n"
                "[green]4[/green]  Search Trace\n"
                "[green]5[/green]  Statistics\n"
                "[green]6[/green]  Export Report\n"
                "[green]7[/green]  Help\n"
                "[green]8[/green]  Exit\n\n"
                "Shortcut Keys:\n"
                "[yellow]h[/yellow] → Help\n"
                "[red]q[/red] → Exit",
                title="INPUT GUIDE",
                border_style="red"
            )
        )


# ==========================================
# RUN TRACE
# ==========================================

def run_trace():

    loading("Running Trace...")

    console.print(
        Panel(
            "[bold green]Trace Execution Successful[/bold green]\n\n"
            "Python File : example.py\n"
            "Status      : Completed\n"
            "Variables   : 12\n"
            "Execution   : Successful",
            title="RUN TRACE",
            border_style="green"
        )
    )


# ==========================================
# VIEW TRACE
# ==========================================

def view_trace():

    console.print(
        Panel(
            "[bold cyan]Saved Trace History[/bold cyan]\n\n"
            "Trace ID : 1\n"
            "File     : example.py\n"
            "Date     : Today\n"
            "Status   : Completed\n\n"
            "Trace ID : 2\n"
            "File     : calculator.py\n"
            "Date     : Today\n"
            "Status   : Completed",
            title="VIEW TRACE",
            border_style="cyan"
        )
    )


# ==========================================
# REPLAY TRACE
# ==========================================

def replay_trace():

    loading("Loading Replay...")

    console.print(
        Panel(
            "[yellow]Step 1[/yellow]\n"
            "x = 10\n\n"

            "[yellow]Step 2[/yellow]\n"
            "y = 20\n\n"

            "[yellow]Step 3[/yellow]\n"
            "z = x + y\n"
            "z = 30\n\n"

            "[bold green]Replay Completed Successfully[/bold green]",
            title="REPLAY TRACE",
            border_style="yellow"
        )
    )


# ==========================================
# SEARCH TRACE
# ==========================================

def search_trace():

    filename = Prompt.ask(
        "[bold cyan]Enter filename[/bold cyan]"
    )

    console.print()

    console.print(
        Panel(
            f"[bold green]Search Results[/bold green]\n\n"
            f"Searching for : {filename}\n\n"
            "Result Found\n"
            "Trace ID : 1\n"
            "Status   : Completed",
            title="SEARCH TRACE",
            border_style="green"
        )
    )
# ==========================================
# STATISTICS
# ==========================================

def statistics():

    console.print(
        Panel(
            "[bold magenta]PROJECT STATISTICS[/bold magenta]\n\n"
            "Total Traces        : 25\n"
            "Python Files        : 10\n"
            "Variables Tracked   : 185\n"
            "Execution Success   : 24\n"
            "Execution Failed    : 1\n"
            "Average Runtime     : 0.18 sec",
            title="STATISTICS",
            border_style="magenta"
        )
    )


# ==========================================
# EXPORT REPORT
# ==========================================

def export_report():

    loading("Exporting Report...")

    console.print(
        Panel(
            "[bold green]Report Exported Successfully[/bold green]\n\n"
            "Format : TXT\n"
            "Location : reports/report.txt",
            title="EXPORT REPORT",
            border_style="green"
        )
    )


# ==========================================
# HELP MENU
# ==========================================

def help_menu():

    console.print(
        Panel(
            "[bold cyan]PYCHRONICLE HELP[/bold cyan]\n\n"

            "[bold yellow]Menu Options[/bold yellow]\n"
            "1 → Run Trace\n"
            "2 → View Trace\n"
            "3 → Replay Trace\n"
            "4 → Search Trace\n"
            "5 → Statistics\n"
            "6 → Export Report\n"
            "7 → Help\n"
            "8 → Exit\n\n"

            "[bold yellow]Keyboard Shortcuts[/bold yellow]\n"
            "h → Help Menu\n"
            "q → Exit Program\n\n"

            "[bold yellow]Instructions[/bold yellow]\n"
            "• Enter only numbers between 1 and 8.\n"
            "• Invalid inputs are rejected.\n"
            "• Follow on-screen instructions.\n"
            "• Reports are stored after export.",
            title="HELP",
            border_style="blue"
        )
    )


# ==========================================
# EXIT PROGRAM
# ==========================================

def exit_program():

    if Confirm.ask("[bold red]Are you sure you want to exit?[/bold red]"):

        loading("Closing Application...")

        console.print(
            Panel.fit(
                Align.center(
                    "[bold green]Thank You![/bold green]\n\n"
                    "[bold cyan]Thank you for using PyChronicle[/bold cyan]\n\n"
                    "Have a wonderful day!"
                ),
                title="EXIT",
                border_style="green"
            )
        )

        return False

    warning("Returning to Main Menu...")
    return True


# ==========================================
# PROCESS USER CHOICE
# ==========================================

def process_choice(choice):

    if choice == 1:
        run_trace()

    elif choice == 2:
        view_trace()

    elif choice == 3:
        replay_trace()

    elif choice == 4:
        search_trace()

    elif choice == 5:
        statistics()

    elif choice == 6:
        export_report()

    elif choice == 7:
        help_menu()

    elif choice == 8:
        return exit_program()

    return True
# ==========================================
# MAIN PROGRAM
# ==========================================

def main():

    console.clear()

    # Welcome Screen
    show_welcome()

    input("\nPress Enter to continue...")

    console.clear()

    # User Guide
    show_instructions()

    input("\nPress Enter to continue...")

    running = True

    while running:

        console.clear()

        display_menu()

        choice = get_choice()

        console.print()

        running = process_choice(choice)

        if running:
            input("\nPress Enter to return to the Main Menu...")


# ==========================================
# PROGRAM ENTRY POINT
# ==========================================

if __name__ == "__main__":
    main()