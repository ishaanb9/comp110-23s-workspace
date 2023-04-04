"""EX06 - Create Your Own Adventure - Country Capitals game!!!!"""


__author__ = "730562389"


from random import randint


points: int = 0
player: str = ""


SMILEY_FACE = "\U0001F604"
SAD_FACE = "\U0001F641"
THUMBS_UP = "\U0001F44D"


def main() -> None:
    "Runs my Capitals quiz game!!"
    topscore = 0
    global points
    global player
    greet()
    start_playing: bool = True
    while start_playing is True:
        input1 = input(f"Welcome {player}!!! Enter 1 to start the game, 2 for extra instructions, and 3 to stop: ")
        input1 = only_possible_values(input1)
        if input1 == "1":
            capitals_game()
            if points > topscore:
                topscore = points
            points = 0
            print(f"Your top score is {topscore}!!!")
        
        if input1 == "2":
            instructions()
        
        if input1 == "3":
            print("Thanks for playing!!!")
            start_playing = False


def only_possible_values(input1 = str) -> str:
    """Makes sure that the player only inputs a number that is part of the function."""
    start_input: bool = False
    while start_input is True:
        if input1 == "1":
            start_input = True
        if input1 == "2":
            start_input = True
        if input1 == "3":
            start_input = True
        else:
            input1 = input("Please enter 1, 2, or 3: ")
    return input1


def greet() -> None:
    """Welcoming the Capital quiz game!"""
    print("Welcome to the capitals quiz game!! In this game you guess the capitals of different countries around the world.")

    global player
    player = input("What is your name? ")


def capitals_game() -> None:
    """Game loop with questions which adds points if you get the question right and does not add anything if you get it wrong."""
    global player
    global points
    print(f"{player}, you are going to start the Capitals game!")
    inputbeginner = input("Beginner 1 - Japan: ")
    if inputbeginner == "Tokyo":
        points += 5
        print(f"Correct {THUMBS_UP}")
    else:
        print(f"Wrong Answer {SAD_FACE}")

    input3 = input("Beginner 2 - France: ")
    if input3 == "Paris":
        points += 5
        print(f"Correct {THUMBS_UP}")
    else:
        print(f"Wrong Answer {SAD_FACE}")

    inputbeginner = input("Beginner 3 - India: ")
    if inputbeginner == "Delhi":
        points += 5
        print(f"Correct {THUMBS_UP}")
    else:
        print(f"Wrong Answer {SAD_FACE}")

    inputbeginner = input("Intermediate 1 - Peru: ")
    if inputbeginner == "Lima":
        points += 5
        print(f"Correct {THUMBS_UP}")
    else:
        print(f"Wrong Answer {SAD_FACE}")

    inputbeginner = input("Intermediate 2 - Croatia: ")
    if inputbeginner == "Zagreb":
        points += 5
        print(f"Correct {THUMBS_UP}")
    else:
        print(f"Wrong Answer {SAD_FACE}")

    inputbeginner = input("Intermediate 3 - Romania: ")
    if inputbeginner == "Bucharest":
        points += 5
        print(f"Correct {THUMBS_UP}")
    else:
        print(f"Wrong Answer {SAD_FACE}")

    inputbeginner = input("Advanced 1 - Nigeria: ")
    if inputbeginner == "Abuja":
        points += 5
        print(f"Correct {THUMBS_UP}")
    else:
        print(f"Wrong Answer {SAD_FACE}")

    inputbeginner = input("Advanced 2 - Malta: ")
    if inputbeginner == "Valletta":
        points += 5
        print(f"Correct {THUMBS_UP}")
    else:
        print(f"Wrong Answer {SAD_FACE}")

    inputbeginner = input("Advanced 3 - Liechtenstein: ")
    if inputbeginner == "Vaduz":
        points += 5
        print(f"Correct {THUMBS_UP}")
    else:
        print(f"Wrong Answer {SAD_FACE}")

    print(f"Points obtained: {points}!")
    print(f"You came in {str(randint(1, 2))} place. Congrats!!")
    print(f"Thanks for playing! {SMILEY_FACE}")


def instructions(instruction_input = int) -> int:
    """Gives players the instructions for the game."""
    global player
    global points
    """Giving instructions for the capitals game!"""
    print("Welcome to the capitals quiz game!! In this game you guess the capitals of different countries around the world.")
    print("1) Type all the capitals by starting with a capital letter for the first letter.")
    print("2) Play the game until the end for 9 levels after which you can view your score.")

    instruction_input = input("Enter 1 to start the game or 3 to stop: ")
    if instruction_input == 1:
        points += 2
    return instruction_input


if __name__ == "__main__":
    main()