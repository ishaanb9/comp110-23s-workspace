"""This is the final step of wordle where we use functions definitions to create the final version of the game!"""


__author__ = "730562389"


def contains_char(wordle_word: str, input_char: str) -> bool:
    """Searches through the length of a guess to see if it contains a certain character."""
    assert len(input_char) == 1  
    char: bool = False
    index: int = 0
    while (index < len(wordle_word)): 
        if (wordle_word[index] == input_char):
            return True
        index += 1
    return char


def emojified(wordle_guess: str, wordle_word: str) -> str:
    """Goes through the length of the guess and assigns each letter with a colored box depending on if the letter is in the correct place, there but not in the correct place, or not there at all."""
    # Asserting that the length of the word is always equal to the length of the guess. 
    assert len(wordle_word) == len(wordle_guess)  

    # Defining the boxes to show if your letter is right, not in the right place or not there at all.
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    WHITE_BOX: str = "\U00002B1C"

    index: int = 0
    wordle_final: str = ""

    # Using the defined function contains_char() to check if the 
    while (index < len(wordle_word)):
        if contains_char(wordle_word, wordle_guess[index]):
            if (wordle_guess[index] == wordle_word[index]):
                wordle_final += GREEN_BOX # Adding a green box when the letter is there and in the right place.
            else:
                wordle_final += YELLOW_BOX # Adding a yellow box when the letter is there but not in the right place.
        else:
            wordle_final += WHITE_BOX # Adding a white box when the letter is not there in the actual word.
        index += 1
    return wordle_final


def input_guess(wordle_length: int) -> str:
    """Prompts user for an input until the tries are over."""

    guess_input: str = input(f"Enter a {wordle_length} character word: ")
    while (len(guess_input) != wordle_length):

        # When the input is not 5 characters it will prompt the user to try with a word with 5 characters. 
        guess_input = input(f"That wasn't {wordle_length} chars! Try again: ")
    return guess_input


def main() -> None:
    """The main loop for the game."""
    SECRET: str = "codes"
    LEN_SECRET: int = len(SECRET)
    number_of_turns: int = 1
    max_turns: int = 6
    wordle_guess: str = ""
    while (number_of_turns <= max_turns):
        # It gives a turn count where the user can keep going until his turns are over or the user gets the word.
        print(f"=== Turn {number_of_turns}/{max_turns} ===")
        wordle_guess = input_guess(LEN_SECRET)
        print(emojified(wordle_guess, SECRET))
        # It is printed when the user guesses the right word. 
        if (wordle_guess == SECRET):
            print(f"You won in {number_of_turns}/{max_turns} turns!")
            number_of_turns = 8
        number_of_turns += 1
        # It is printed when the user has used up maximum number of tries.
    if (number_of_turns == 7):
        print(f"X/{max_turns} - Sorry, try again tomorrow!")


if (__name__ == "__main__"):
    main()
 