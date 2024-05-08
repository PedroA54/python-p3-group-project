# lib/helpers.py

EXIT_WORDS = ["0", "exit", "quit"]

def welcome():
    print("""
    _   ______  ___       __________  ___   ________ __ __________ 
   / | / / __ )/   |     /_  __/ __ \/   | / ____/ //_// ____/ __ \
  /  |/ / __  / /| |      / / / /_/ / /| |/ /   / ,<  / __/ / /_/ /
 / /|  / /_/ / ___ |     / / / _, _/ ___ / /___/ /| |/ /___/ _, _/ 
/_/ |_/_____/_/  |_|    /_/ /_/ |_/_/  |_\____/_/ |_/_____/_/ |_|  
                                                                   """, style= "heading")
    
def how_to_use():
    print("Welcome to NBA Stat Tracker!", style="subhead")
    print("Here is how it works:", style="subhead")
    print("1. Select 'Get Started'")
    print("""2. Choose what statistics you would like to see: Choose from a team's current seasonal record
          or their starting roster""")
    print("3. Search what team whose statistics you'd like to see by their name.")
    print("4. Have Fun!")

def start():
    print("Please select an option:", style="subhead")
    print("0. Exit the program")
    print("1. Track Teams")
    print("2. Track Teams Starting Roster")
    print("3. Delete User")



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