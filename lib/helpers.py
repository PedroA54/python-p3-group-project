# lib/helpers.py
# from models.user import User
from models.players import Players
from models.teams import Team
from seed import start_program
from rich.console import Console
from time import sleep
import click
import csv


console = Console()
EXIT_WORDS = ["5", "exit", "quit"]


def welcome():
    click.clear()
    console.rule("[bold purple] NBA-STASTICS :basketball:")


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
        """2. Choose what statistics you would like to see: Choose from a team's current seasonal record their starting roster"""
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


def team_stats():
    while True:

        console.print(
            "Please select an option: ", style="bold underline purple on white"
        )
        console.print("1. All teams")
        console.print("2.")
        console.print("3. Exit the program")

        user_input = input("> ").strip().lower()

        if user_input in EXIT_WORDS:
            exit_program()
        elif user_input == "1":
            all_teams()
        elif user_input == "2":
            pass
        elif user_input == "3":
            exit_program()


def load_teams_from_csv(filename):
    teams = []

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            team = Team(
                row["NbaTeam"],
                row["City"],
                int(row["Wins"]),
                int(row["Losses"]),
                int(row["Championchips"]),
                row["PG"],
                row["SG"],
                row["SF"],
                row["PF"],
                row["C"],
            )
            teams.append(team)

    return teams


def all_teams():
    teams = load_teams_from_csv("lib/data/team.csv")

    console.print("All NBA Teams:\n")
    for team in teams:
        console.print(f"Team: {team.nba_team}")
        console.print(f"City: {team.city}")
        console.print(f"Wins: {team.wins}")
        console.print(f"Losses: {team.losses}")
        console.print(f"Championships: {team.championships}")
        console.print(f"PG: {team.pg}")
        console.print(f"SG: {team.sg}")
        console.print(f"SF: {team.sf}")
        console.print(f"PF: {team.pf}")
        console.print(f"C: {team.c}")
        console.print()

def load_players_from_csv(filename):
    players = []

    with open(filename, "r", newline="") as file:
         reader = csv.DictReader(file)
         for row in reader:
            player = Players(
                row["Name"],
                row["Team"],
                row["Position"],
                int(row["Points"]),
                int(row["Assists"]),
                int(row["Rebounds"]),
            )
            players.append(player)

    return players


def team_roster():
    search_name = input("Enter player name to search: ").strip()

    players = load_players_from_csv("lib/data/player.csv")

    found_players = [player for player in players if player.name.lower() == search_name.lower()]

    if not found_players:
        console.print(f"No player found with the name '{search_name}'")
        return

    console.print(f"Players found with the name '{search_name}':\n")

    for player in found_players:
        console.print(f"Name: {player.name}")
        console.print(f"Team: {player.team}")
        console.print(f"Position: {player.position}")
        console.print(f"Points: {player.points}")
        console.print(f"Assists: {player.assists}")
        console.print(f"Rebounds: {player.rebounds}")
        console.print()



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
