def display_menu():
    print("\n========== PyChronicle CLI ==========")
    print("1. Run Trace")
    print("2. View Trace")
    print("3. Replay Trace")
    print("4. Help")
    print("5. Exit")
    print("=====================================")


def process_choice(choice):
    if choice == 1:
        print("\nRunning Trace...")
    elif choice == 2:
        print("\nOpening Trace Viewer...")
    elif choice == 3:
        print("\nReplaying Trace...")
    elif choice == 4:
        print("\nHelp")
        print("Choose an option from 1 to 5.")
    elif choice == 5:
        print("\nThank you for using PyChronicle!")


display_menu()

try:
    choice = int(input("Enter your choice (1-5): "))

    if 1 <= choice <= 5:
        process_choice(choice)
    else:
        print("Error: Please enter a number between 1 and 5.")

except ValueError:
    print("Error: Invalid input. Please enter numbers only.")