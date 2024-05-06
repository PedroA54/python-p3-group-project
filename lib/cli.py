# lib/cli.py
from helpers import (
welcome,
how_to_use,
start,
create_user,
delete_user,
exit_program, 
)

def main():
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
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice!")


def menu():
    print("Please select an option:")
    print("0. Exit")
    print("1. How To Use")
    print("2. Get Started")
    print("3. Create User")
    print("4. Delete User")


if __name__ == "__main__":
    welcome()
    main()
