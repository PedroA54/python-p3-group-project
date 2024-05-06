# lib/helpers.py
from rich.console import Console

console = Console()
EXIT_WORDS = ["0", "exit", "quit"]


def welcome():
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


def how_to_use():
    console.print("Welcome to NBA Stat Tracker!", style="subhead")
    console.print("Here is how it works:", style="subhead")
    console.print("1. Select 'Get Started'")
    console.print(
        """2. Choose what statistics you would like to see: Choose from a team's current seasonal record
          or their starting roster"""
    )
    console.print(
        "3. Search what team whose statistics you'd like to see by their name."
    )
    console.print("4. Have Fun!")


def start():
    console.print("Please select an option:", style="subhead")
    console.print("0. Exit the program")
    console.print("1. Track Teams")
    console.print("2. Track Teams Starting Roster")
    console.print("3. Delete User")


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


def exit_program():
    print("Goodbye!")
    exit()


def play_game():
    pass
