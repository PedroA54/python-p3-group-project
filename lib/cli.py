# lib/cli.py

from helpers import exit_program, create_user, helper_2, helper_3

EXIT_WORDS = ["4", "exit", "quit", "c"]


def main():
    while True:
        menu()
        choice = input(">")
        if choice in EXIT_WORDS:
            exit_program()
        elif choice == "1":
            create_user()
        elif choice == "2":
            helper_2()
        elif choice == "3":
            helper_3()
        elif choice == "4":
            exit_program()
        else:
            print("Invalid input")


def menu():
    print("Please select an option:")
    print("1. Create User")
    print("2. Some useful function")
    print("3. Some useful function")
    print("4. Exit the program")


if __name__ == "__main__":
    main()
