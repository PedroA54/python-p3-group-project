# lib/cli.py
from helpers import (
    welcome,
    menu,
    how_to_use,
    start,
    exit_program,
    find_or_create_username,
)

EXIT_WORDS = ["4", "exit", "quit"]


def main():
    welcome()
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            how_to_use()
        elif choice == "2":
            start()
        elif choice == "3":
            user = find_or_create_username()
        elif choice == "4":
            exit_program()
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
