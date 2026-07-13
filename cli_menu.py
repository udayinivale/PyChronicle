def display_menu():
    print("\n========== PyChronicle CLI ==========")
    print("1. Run Trace")
    print("2. View Trace")
    print("3. Replay Trace")
    print("4. Help")
    print("5. Exit")
    print("=====================================")

def handle_choice(choice):
    if choice == "1":
        print("\nRunning Trace...")
    elif choice == "2":
        print("\nViewing Trace...")
    elif choice == "3":
        print("\nReplaying Trace...")
    elif choice == "4":
        print("\nHelp:")
        print("Choose an option from 1 to 5.")
    elif choice == "5":
        print("\nExiting PyChronicle...")
    else:
        print("\nInvalid choice!")

display_menu()
choice = input("Enter your choice: ")
handle_choice(choice)