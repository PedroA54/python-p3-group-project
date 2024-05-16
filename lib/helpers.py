# lib/helpers.py
from models import CURSOR, CONN
from models.players import Players
from models.teams import Team
from models.user import User
from seed import start_program
from rich.console import Console
import click


console = Console()
EXIT_WORDS = ["exit", "quit"]


def welcome():
    click.clear()
    console = Console()
    console.rule("[bold purple] NBA-STASTICS 23/24 :basketball:")
    console.print(
        """  
  _  _ ___   _     _____ ___    _   ___ _  _____ ___ 
 | \| | _ ) /_\   |_   _| _ \  /_\ / __| |/ / __| _ \\
 | .` | _ \/ _ \    | | |   / / _ \ (__| ' <| _||   /
 |_|\_|___/_/ \_\   |_| |_|_\/_/ \_\___|_|\_\___|_|_\\
                                                     
""",
        style="blue",
    )


# mainMenu
def menu():
    console.print("Please select an option: ", style="bold underline purple on white")
    console.print("1. How To Use")
    console.print("2. Get Started")
    console.print("3. Create user")
    console.print("4. Exit")


# subMenu1
def start():
    while True:
        console.print(
            "Please select an option: ", style="bold underline purple on white"
        )
        console.print("1. Track Teams")
        console.print("2. Player Search")
        console.print("3. Manage user")
        console.print("4. Exit the program")

        user_input = input("> ").strip().lower()

        if user_input in EXIT_WORDS:
            exit_program()
        elif user_input == "1":
            team_stats()
        elif user_input == "2":
            team_roster()
        elif user_input == "3":
            manage_users()
        elif user_input == "4":
            exit_program()
        else:
            print("Invalid choice!")


def how_to_use():
    console.print("Welcome to NBA Stat Tracker!")
    console.print("Here is how it works: ", style="bold underline purple on white")
    console.print("4. Create 'User'")
    console.print("1. Select 'Get Started'")
    console.print("2. Choose to view 'Team' statistics ")
    console.print("3. Choose to view 'Player' statistics")
    console.print("4. Have Fun!")


def load_teams_from_db():
    teams = []
    try:
        with CONN:
            CURSOR.execute("SELECT * FROM teams")
            rows = CURSOR.fetchall()
            for row in rows:
                team = Team(*row)
                teams.append(team)
    except Exception as e:
        print("Error loading teams from database:", e)
    return teams


def team_stats():
    teams = load_teams_from_db()
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
        console.print("4. Search team by City")
        console.print("5. Add player to a team")
        console.print("6. Remove player from a team")
        console.print("7. Exit the program")

        user_input = input("> ").strip().lower()

        if user_input in EXIT_WORDS:
            exit_program()
        elif user_input == "1":
            current_page = all_teams(teams, current_page, teams_per_page)
        elif user_input == "2":
            east_team(current_page, teams_per_page)
        elif user_input == "3":
            west_team(current_page, teams_per_page)
        elif user_input == "4":
            search_team()
        elif user_input == "5":
            add_player_to_team(teams)
        elif user_input == "6":
            remove_player_from_team(teams)
        elif user_input == "7":
            exit_program()


def all_teams(teams, page_number, teams_per_page):
    teams = load_teams_from_db()
    while True:
        start_index = (page_number - 1) * teams_per_page
        end_index = min(start_index + teams_per_page, len(teams))
        console.print("[bold #FF7EF5]All NBA Teams[/bold #FF7EF5]")
        console.print(f" Page {page_number}\n")
        print("==================")
        for team in teams[start_index:end_index]:
            console.print(f"Team: {team.team}")
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


def east_team(page_number, teams_per_page=5):
    teams = load_teams_from_db()
    while True:
        start_index = (page_number - 1) * teams_per_page
        end_index = min(start_index + teams_per_page, len(teams))
        console.print("[bold #FF7EF5]East NBA Teams[/bold #FF7EF5]")
        console.print(f" Page {page_number}\n")
        print("==================")
        for team in teams[0:14][start_index:end_index]:
            console.print(f"Team: {team.team}")
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


def west_team(page_number, teams_per_page=5):
    teams = load_teams_from_db()
    while True:
        start_index = (page_number - 1) * teams_per_page
        end_index = min(start_index + teams_per_page, len(teams))
        console.print("[bold #FF7EF5]West NBA Teams[/bold #FF7EF5]")
        console.print(f" Page {page_number}\n")
        print("==================")
        for team in teams[15:31][start_index:end_index]:
            console.print(f"Team: {team.team}")
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
        elif choice.lower() == "n" and (start_index + teams_per_page) < len(
            teams[15:31]
        ):
            page_number += 1
        elif choice.lower() == "x":
            break


def search_team():
    city = input("Enter the name of the City: ").strip()
    found_team = Team.find_by_city(city)
    if found_team:
        console.print(f"Team: {found_team.team}")
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
        console.print(f"No team found in city '{city}'.")


def add_player_to_team(teams):

    player_name = input("Enter player name to add to team: ").strip()

    player = Players.find_by_name(player_name)
    if player is None:
        console.print(f"No player found with the name '{player_name}'")
        return

    team_name = input("Enter team name to add player to: ").strip()
    team = Team.find_by_name(team_name)

    if team is None:
        console.print(f"No team found with the name '{team_name}'")
        return

    try:

        player.team_id = team.id

        player.save()

        console.print(f"Added player {player.name} to team {team.team}")
    except Exception as e:
        print("Error adding player to team:", e)


def remove_player_from_team(teams):
    team_name = input("Enter the name of the team: ").strip()
    player_name = input("Enter the name of the player to remove: ").strip()

    try:
        player = player.find_by_name()
        console.print(f"Player '{player_name}' removed from team '{team_name}'.")
    except Exception as e:
        print("Error removing player from team:", e)


def load_players_from_db():
    players = []
    try:
        with CONN:
            CURSOR.execute("SELECT * FROM players")
            rows = CURSOR.fetchall()
            for row in rows:
                player = Players(
                    row[1],
                    row[2],
                    row[3],
                    float(row[4]),
                    float(row[5]),
                    float(row[6]),
                    row[0],
                )
                players.append(player)
    except Exception as e:
        print("Error loading players from database:", e)
    return players


def team_roster():
    search_name = input("Enter player name to search: ").strip()

    players = load_players_from_db()

    found_players = [
        player for player in players if player.name.lower() == search_name.lower()
    ]

    if not found_players:
        console.print(f"No player found with the name '{search_name}'")
        return

    console.print(f"Players found with the name '{search_name}':\n")

    for player in found_players:
        try:
            team = Team.find_by_id(player.team_id)
            team_name = team.team if team else "Unknown"
        except Exception as e:
            print(f"Error finding team for player {player.name}: {e}")
            team_name = "Unknown"

        console.print(f"Name: {player.name}")
        console.print(f"Team: {team_name}")
        console.print(f"Position: {player.position}")
        console.print(f"Points: {player.points}")
        console.print(f"Assists: {player.assists}")
        console.print(f"Rebounds: {player.rebounds}")
        console.print()


def manage_users():
    while True:
        console.print(
            "Please select an option: ", style="bold underline purple on white"
        )
        console.print("1. Create user")
        console.print("2. Delete user")
        console.print("3. Exit")

        user_input = input("> ").strip().lower()

        if user_input in EXIT_WORDS:
            exit_program()
        elif user_input == "1":
            create_user()
        elif user_input == "2":
            delete_user()
        elif user_input == "3":
            exit_program()
        else:
            print("Invalid choice!")


def create_user():
    name = input("Enter your name: ").strip()

    if name.lower() in EXIT_WORDS:
        exit_program()

    player = User.find_by_name(name)

    if player is None:
        new_player = User.create(name)
        print(f"Welcome, {new_player.name}!")
        start()
    else:
        print(f"Welcome back, {player.name}!")
        start()


def delete_user():
    try:
        name = input("Enter the name of the user you want to delete: ").strip()

        if name.lower() in EXIT_WORDS:
            exit_program()

        if not name:
            print("Name cannot be empty. Please try again.")
            delete_user()

        # Assuming EXIT_WORDS is defined somewhere in your code
        player = User.find_by_name(name)

        if player:
            player.delete()
        else:
            print(f"Could not find {name}.")
    except Exception as e:
        print("An error occurred:", e)


def exit_program():
    print("Goodbye!")
    exit()
