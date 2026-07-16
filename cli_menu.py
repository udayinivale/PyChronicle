def display_menu():
    print("\n========== PyChronicle ==========")
    print("Welcome to PyChronicle!")
    print("Please select an option:\n")

    print("1. Run Trace")
    print("2. View Trace")
    print("3. Replay Trace")
    print("4. Help")
    print("5. Exit")

    print("=================================")


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
        print("\nRunning Trace...")
        print("Please wait while the trace is being generated.")

    elif choice == 2:
        print("\nOpening Trace Viewer...")
        print("Loading saved execution trace...")

    elif choice == 3:
        print("\nReplaying Trace...")
        print("Preparing replay...")

    elif choice == 4:
        print("\nHelp")
        print("Choose an option from 1 to 5.")
        print("Follow the instructions displayed on the screen.")

    elif choice == 5:
        print("\nThank you for using PyChronicle!")
        return False

    return True


running = True

while running:
    display_menu()
    choice = get_choice()
    running = process_choice(choice)