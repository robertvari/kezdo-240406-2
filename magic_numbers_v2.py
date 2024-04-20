import random, os

# Globals
MAX_NUMBER = 10
PLAYER_NAME = None
CREDITS = 10

def main():
    clear_screen()
    intro()

    player_input = ask_for_start_game("Are your ready?")

    if player_input != "y":
        print("Have a nice day.")
        exit()

    # Start game

def clear_screen():
    os.system("cls")

def intro():
    print("*"*50, "Magic Numbers".upper(), "*"*50)

    get_player_name()

    print(f"Hello {PLAYER_NAME}!")
    print(f"I guess a number between 1 and {MAX_NUMBER}.")
    print("If you win, you get 10 credits. If you loose, I get 10 credits.")
    print("I give you 10 credits for a start.")
    print("*"*50)

def get_player_name():
    # Import global PLAYER_NAME into this scope
    global PLAYER_NAME
    PLAYER_NAME = input("What is your name?")

def ask_for_start_game(question):
    return input(f"{question} (y/n)")


# Call main() and start program
main()