# lib/cli.py
from helpers import (
    menu,
    how_to_use,
    start,
    create_user,
    delete_user,
    exit_program,
)

EXIT_WORDS = ["4", "exit", "quit"]


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            how_to_use()
        elif choice == "1":
            start()
        elif choice == "2":
            create_user()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            exit_program()
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
