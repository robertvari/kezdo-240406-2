import random, os

# Globals
MAX_NUMBER = 10
PLAYER_NAME = None
CREDITS = 30

def main():
    clear_screen()
    intro()

    player_input = ask_for_start_game("Are your ready?")

    if player_input != "y":
        print("Have a nice day.")
        exit()

    # Start game
    game_loop()

def clear_screen():
    os.system("cls")

def intro():
    print("*"*50, "Magic Numbers".upper(), "*"*50)

    get_player_name()

    print(f"Hello {PLAYER_NAME}!")
    print(f"I guess a number between 1 and {MAX_NUMBER}.")
    print("If you win, you get 10 credits. If you loose, I get 10 credits.")
    print(f"I give you {CREDITS} credits for a start.")
    print("*"*50)

def get_player_name():
    # Import global PLAYER_NAME into this scope
    global PLAYER_NAME
    PLAYER_NAME = input("What is your name?")

def ask_for_start_game(question):
    return input(f"{question} (y/n)")

def game_loop():
    global CREDITS

    try_counter = 3

    # Generate a random number
    magic_number = random.randint(1, MAX_NUMBER)

    # Get player number
    player_number = input("Guess my number:")
    
    while str(magic_number) != player_number:
        try_counter -= 1

        if try_counter == 0:
            break

        print(f"Wrong guess! You have {try_counter} tries left. Try again.")
        player_number = input("Guess my number:")

    # End game conditions
    if str(magic_number) == player_number:
        print(f"You win! {magic_number} was my number :)")
        CREDITS += 10
    else:
        print(f"You lost the game :( My number was {magic_number}")
        CREDITS -= 10

        if CREDITS <= 0:
            print(f"I'm sorry {PLAYER_NAME}. You lost all your credits. Game Over:(")
            exit()
    
    print(f"Now you have {CREDITS} credits")

    # Ask player for a new game
    player_input = ask_for_start_game("Do you want to play agai?")

    if player_input != "y":
        print("Have a nice day.")
        exit()
    
    # Start new game
    clear_screen()
    game_loop()



# Call main() and start program
main()