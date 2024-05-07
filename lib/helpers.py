# lib/helpers.py
from models.teams import Team
from seed import start_program
from rich.console import Console
import click
import csv


console = Console()
EXIT_WORDS = ["exit", "quit"]


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
        console.print("3. Function")
        console.print("4. Exit the program")

        user_input = input("> ").strip().lower()

        if user_input in EXIT_WORDS:
            exit_program()
        elif user_input == "1":
            team_stats()
        elif user_input == "2":
            team_roster()
        elif user_input == "3":
            pass
        elif user_input == "4":
            exit_program()
        else:
            print("Invalid choice!")


def team_stats():
    teams = load_teams_from_csv("lib/data/team.csv")

    while True:

        console.print(
            "Please select an option: ", style="bold underline purple on white"
        )
        console.print("1. All teams")
        console.print("2. East")
        console.print("3. West")
        console.print("4. Search team by Name")
        console.print("5. Exit the program")

        user_input = input("> ").strip().lower()

        if user_input in EXIT_WORDS:
            exit_program()
        elif user_input == "1":
            all_teams()
        elif user_input == "2":
            east_team()
        elif user_input == "3":
            west_team()
        elif user_input == "4":
            search_team(teams)  # grabs data from team.csv
        elif user_input == "5":
            exit_program()
        else:
            print("Invalid choice!")


# Gets Data from team.csv
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


# Gets all teams
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


# Gets teams only the East
def east_team():
    teams = load_teams_from_csv("lib/data/team.csv")

    console.print("East NBA Teams:\n")
    for team in teams[0:15]:
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


# Gets team only on the west
def west_team():
    teams = load_teams_from_csv("lib/data/team.csv")

    console.print("West NBA Teams:\n")
    for team in teams[16:31]:
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


# Searches Team by Name
def search_team(teams):
    team_name = input("Enter the name of the team: ").strip()
    found_team = None
    for team in teams:
        if team.nba_team.lower() == team_name.lower():
            found_team = team
            break

    if found_team:
        console.print(f"Team: {found_team.nba_team}")
        console.print(f"City: {found_team.city}")
        console.print(f"Wins: {found_team.wins}")
        console.print(f"Losses: {found_team.losses}")
        console.print(f"Championships: {found_team.championships}")
        console.print(f"PG: {found_team.pg}")
        console.print(f"SG: {found_team.sg}")
        console.print(f"SF: {found_team.sf}")
        console.print(f"PF: {found_team.pf}")
        console.print(f"C: {found_team.c}")
    else:
        console.print(f"No team found with the name '{team_name}'.")


def team_roster():
    pass


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
