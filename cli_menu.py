from rich import print
from rich.table import Table
from rich.panel import Panel
from rich.console import Console

console = Console()

def display_menu():
    # Week 3 Day 2 Formatting: Replacing basic text with a formatted Rich Table
    table = Table(title="PYCHRONICLE UI", title_style="bold cyan", show_header=True, header_style="bold magenta")
    table.add_column("Option", justify="center", style="green", width=6)
    table.add_column("Action Description", justify="left", style="white")

    table.add_row("1", "Run Trace")
    table.add_row("2", "View Trace")
    table.add_row("3", "Replay Trace")
    table.add_row("4", "Help")
    table.add_row("5", "Exit")

    print("") # Padding spacing
    console.print(table)

def get_choice():
    while True:
        user_input = input("\nSelect an option (1-5): ").strip()

        if user_input == "":
            print("[bold red]Error:[/bold red] Input cannot be empty.")
            continue

        if not user_input.isdigit():
            print("[bold red]Error:[/bold red] Please enter numbers only.")
            continue

        choice = int(user_input)

        if 1 <= choice <= 5:
            return choice
        else:
            print("[bold red]Error:[/bold red] Please enter a number between 1 and 5.")

def process_choice(choice):
    print("") # Formatting separation spacing
    
    if choice == 1:
        print("[yellow]Running Trace...[/yellow]")

    elif choice == 2:
        print("[yellow]Opening Trace Viewer...[/yellow]")

    elif choice == 3:
        print("[yellow]Replaying Trace...[/yellow]")

    elif choice == 4:
        # Formatted help panel block
        console.print(Panel("[bold blue]Help Menu[/bold blue]\nUse options 1-3 to manage code execution traces.", border_style="blue"))

    elif choice == 5:
        confirm = input("Are you sure you want to exit? (y/n): ").lower().strip()

        if confirm == "y":
            print("[bold green]Thank you for using PyChronicle![/bold green]")
            return False
        else:
            print("[yellow]Returning to menu...[/yellow]")

    return True

if __name__ == "__main__":
    running = True
    while running:
        display_menu()
        choice = get_choice()
        running = process_choice(choice)