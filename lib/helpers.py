# lib/helpers.py
from models.teams import Team
from models.user import User
from seed import start_program
from rich.console import Console
import click
import csv
import sys


console = Console()
EXIT_WORDS = ["exit", "quit"]


def welcome():
    click.clear()
    console.rule("[bold purple] NBA-STASTICS :basketball:")


# mainMenu
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
    console.print("3. Create username")
    console.print("4. Exit")


# subMenu1
def start():
    while True:

        console.print(
            "Please select an option: ", style="bold underline purple on white"
        )
        console.print("1. Track Teams")
        console.print("2. Track Teams Starting Roster")
        console.print("3. Manage users")
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


import sys


import sys


def team_stats():
    teams = load_teams_from_csv("lib/data/team.csv")
    total_teams = len(teams)
    current_page = 1
    teams_per_page = 5

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
            current_page = all_teams(teams, current_page, teams_per_page)
        elif user_input == "2":
            east_team()
        elif user_input == "3":
            west_team()
        elif user_input == "4":
            search_team(teams)
        elif user_input == "5":
            exit_program()
        else:
            print("Invalid choice!")

        sys.stdin.flush()


def all_teams(teams, page_number, teams_per_page):
    while True:
        start_index = (page_number - 1) * teams_per_page
        end_index = min(start_index + teams_per_page, len(teams))
        console.print("[bold #FF7EF5]All NBA Teams[/bold #FF7EF5]")
        console.print(f" Page {page_number}\n")
        print("==================")
        for team in teams[start_index:end_index]:
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

        choice = input(
            "\nEnter your choice (p: Previous Page, n: Next Page, x: Back to Menu): "
        )
        if choice.lower() == "p" and page_number > 1:
            page_number -= 1
        elif choice.lower() == "n" and (start_index + teams_per_page) < len(teams):
            page_number += 1
        elif choice.lower() == "x":
            break


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


def find_or_create_username():
    while True:  # Loop until a valid username is provided or the user chooses to exit
        user_name = input("Enter your username: ").strip()

        if user_name.lower() in EXIT_WORDS:
            exit_program()

        user = User.find_by_name(user_name)

        if user is None:
            try:
                user = User(user_name)
                user.save()
                print(f"Hi, {user_name}!")
                return user  # Exit the loop and return the user object
            except (TypeError, ValueError) as e:
                print(e)
        else:
            print(f"Welcome back, {user_name}!")
            return user  # Exit the loop and return the existing user object
    pass


def delete_user():

    pass


def exit_program():
    print("Goodbye!")
    exit()
