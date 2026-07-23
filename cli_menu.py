from rich import print
from rich.table import Table
from rich.panel import Panel
from rich.console import Console

console = Console()

def display_menu():
    
    table = Table(
        title="PYCHRONICLE UI", 
        title_style="bold cyan", 
        show_header=True, 
        header_style="bold magenta"
    )
    table.add_column("Key / Option", justify="center", style="green", width=14)
    table.add_column("Action Description", justify="left", style="white")

    table.add_row("1", "Run Trace")
    table.add_row("2", "View Trace")
    table.add_row("3", "Replay Trace")
    table.add_row("4 or 'h'", "Help Menu (Shortcut: h)")
    table.add_row("5 or 'q'", "Exit Program (Shortcut: q)")

    print("")  # Padding spacing
    console.print(table)

def get_choice():
    """
    Week 3 Day 3: Keyboard Shortcuts Handling
    Supports number keys (1-5) and hotkeys ('h' for help, 'q' for quit).
    """
    # Shortcut mappings to internal choice numbers
    SHORTCUTS = {
        'h': 4,
        'q': 5
    }

    while True:
        user_input = input("\nSelect option or shortcut (1-5, h, q): ").strip().lower()

        if user_input == "":
            print("[bold red]Error:[/bold red] Input cannot be empty.")
            continue

        # Check if the input matches a defined keyboard shortcut
        if user_input in SHORTCUTS:
            return SHORTCUTS[user_input]

        # Check if the input is a valid number choice
        if user_input.isdigit():
            choice = int(user_input)
            if 1 <= choice <= 5:
                return choice
            else:
                print("[bold red]Error:[/bold red] Please enter a number between 1 and 5.")
                continue

        print("[bold red]Error:[/bold red] Invalid input! Use 1-5, 'h' for help, or 'q' to quit.")

def process_choice(choice):
    print("")  # Formatting separation spacing
    
    if choice == 1:
        print("[yellow]Running Trace...[/yellow]")

    elif choice == 2:
        print("[yellow]Opening Trace Viewer...[/yellow]")

    elif choice == 3:
        print("[yellow]Replaying Trace...[/yellow]")

    elif choice == 4:
        # Formatted help panel block
        console.print(
            Panel(
                "[bold blue]Help Menu & Shortcuts[/bold blue]\n\n"
                "• Options 1-3: Manage code execution traces.\n"
                "• Press [bold green]'h'[/bold green] anytime for Help.\n"
                "• Press [bold green]'q'[/bold green] anytime to Exit quickly.",
                border_style="blue"
            )
        )

    elif choice == 5:
        confirm = input("Are you sure you want to exit? (y/n): ").lower().strip()

        if confirm == "y" or confirm == "q":
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