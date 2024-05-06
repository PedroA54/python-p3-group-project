# lib/helpers.py
from rich.console import Console

console = Console()
EXIT_WORDS = ["4", "exit", "quit", "c"]


def menu():
    print("Please select an option:")
    print("1. Create User")
    print("2. Some useful function")
    print("3. Some useful function")
    print("4. Exit the program")


def create_user():
    print("Creating a new user...")
    name = input("Enter user's name: ")
    email = input("Enter user's email: ")
    print(f"User '{name}' with email '{email}' created successfully.")


def helper_2():
    print("Performing useful function#1.")


def helper_3():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()
