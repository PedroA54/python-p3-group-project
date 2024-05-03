# lib/cli.py
from helpers import (
    welcome,
    menu,
)


def main():
    welcome()
    while True:
        menu()
        choice = input("> ")


if __name__ == "__main__":
    main()
