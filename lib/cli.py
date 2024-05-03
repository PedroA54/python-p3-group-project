# lib/cli.py

from helpers import exit_program, helper_1, helper_2, helper_3


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        elif choice == "2":
            helper_2()
        elif choice == "3":
            helper_3()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")
    print("2. Some useful function")
    print("3. Some useful function")


if __name__ == "__main__":
    main()
