# lib/cli.py
from models.players import Players
from models.teams import Team
from models.user import User
from helpers import (
    welcome,
    menu,
    how_to_use,
    start,
    exit_program,
    create_user,
    delete_user,
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
            create_user()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            exit_program()
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
