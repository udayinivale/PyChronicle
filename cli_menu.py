from rich import print

def display_menu():
    options = [
        "1. Run Trace",
        "2. View Trace",
        "3. Replay Trace",
        "4. Help",
        "5. Exit"
    ]

    print("\n" + "=" * 40)
    print("         PYCHRONICLE")
    print("=" * 40)

    for option in options:
        print(option)

    print("=" * 40)

def get_choice():
    while True:
        user_input = input("\nSelect an option (1-5): ").strip()

        if user_input == "":
            print("Error: Input cannot be empty.")
            continue

        if not user_input.isdigit():
            print("Error: Please enter numbers only.")
            continue

        choice = int(user_input)

        if 1 <= choice <= 5:
            print(f"You selected option {choice}")
            return choice
        else:
            print("Error: Please enter a number between 1 and 5.")


def process_choice(choice):
    if choice == 1:
        print("Running Trace...")

    elif choice == 2:
        print("Opening Trace Viewer...")

    elif choice == 3:
        print("Replaying Trace...")

    elif choice == 4:
        print("Help")

    elif choice == 5:
        confirm = input("Are you sure you want to exit? (y/n): ").lower()

        if confirm == "y":
            print("Thank you for using PyChronicle!")
            return False
        else:
            print("Returning to menu...")

    return True


running = True

while running:
    display_menu()
    choice = get_choice()
    running = process_choice(choice)