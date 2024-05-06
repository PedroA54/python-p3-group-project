# lib/helpers.py
# from models.user import User
# from models.players import Players
# from models.teams import Teams
from seed import start_program
from rich.console import Console
from time import sleep
import click


console = Console()
EXIT_WORDS = ["5", "exit", "quit"]


def welcome():
    click.clear()
    console.rule("[bold purple] NBA-Statistics :basketball:")


def menu():
    console.print(
        """
    _   ______  ___       __________  ___   ________ __ __________ 
   / | / / __ )/   |     /_  __/ __ \/   | / ____/ //_// ____/ __ \
  /  |/ / __  / /| |      / / / /_/ / /| |/ /   / ,<  / __/ / /_/ /
 / /|  / /_/ / ___ |     / / / _, _/ ___ / /___/ /| |/ /___/ _, _/ 
/_/ |_/_____/_/  |_|    /_/ /_/ |_/_/  |_\____/_/ |_/_____/_/ |_|  
                                                                   """,
        style="green",
    )

    console.print("Please select an option: ", style="bold underline purple on white")
    console.print("1. How To Use")
    console.print("2. Get Started")
    console.print("3. Create User")
    console.print("4. Delete User")
    console.print("5. Exit")


def how_to_use():
    console.print("Welcome to NBA Stat Tracker!")
    console.print("Here is how it works: ", style="bold underline purple on white")
    console.print("1. Select 'Get Started'")
    console.print(
        """2. Choose what statistics you would like to see: Choose from a team's current seasonal recordor their starting roster"""
    )
    console.print(
        "3. Search what team whose statistics you'd like to see by their name."
    )
    console.print("4. Have Fun!")


def start():
    while True:

        console.print(
            "Please select an option: ", style="bold underline purple on white"
        )
        console.print("1. Track Teams")
        console.print("2. Track Teams Starting Roster")
        console.print("3. Delete User")
        console.print("4. Exit the program")

        user_input = input("> ").strip().lower()

        if user_input in EXIT_WORDS:
            exit_program()
        elif user_input == "1":
            team_stats()
        elif user_input == "2":
            team_roster()
        elif user_input == "3":
            delete_user()
        elif user_input == "4":
            exit_program()


def create_user():
    # name = input("Enter your name: ").strip()

    # if name.lower() in EXIT_WORDS:
    #     exit_program()

    # player = User.find_by_name(name)

    # if player is None:
    #     new_player = User.create(name)
    #     print(f"Welcome, {new_player.name}!", style="subhead")
    #     play_game(new_player)
    # else:
    #     print(f"Welcome back, {player.name}!", style="subhead")
    #     play_game(player)
    pass


def delete_user():
    # name = input("Enter your name: ").strip()

    # if name.lower() in EXIT_WORDS:
    #     exit_program()

    # player = User.find_by_name(name)
    # if player:
    #     player.delete()
    # else:
    #     print(f"Could not find {name}.", style="subhead")
    pass


def team_stats():
    pass


def team_roster():
    pass


def exit_program():
    print("Goodbye!")
    exit()


def play_game():
    pass
