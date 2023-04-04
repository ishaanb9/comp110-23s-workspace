"""This is the next step towards wordle which includes boxes that indicate if we have a right letter through colors!"""

__author__ = "730562389"

# Declaring the variable for the green, yellow, and white box.
SECRET_WORD: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Declaring variable to use in while loop
letter_count: int = 0
boxes: str = ""

# Ask user for input
guess: str = input("What is your " + str(len(SECRET_WORD)) + " letter guess? ")

# Check if input length if 6 letters
while len(guess) != len(SECRET_WORD):
    guess = input("That was not " + str(len(SECRET_WORD)) + " letters! Try again: ")
    
# While loop to check if letter is in right spot and assign it a green box
while letter_count < len(SECRET_WORD):
    if (SECRET_WORD[letter_count] == guess[letter_count]):
        boxes = boxes + GREEN_BOX
    # Alternate index (yellow_count) to go through all the letters in the word again. 
    else: 
        yellow_correct: bool = False
        yellow_count: int = 0
    # To give yellow box when the letter is in secret word but not in right place and white box when letter is not in the word
        while yellow_count < len(SECRET_WORD) and not yellow_correct:
            if (SECRET_WORD[yellow_count] == guess[letter_count]):
                yellow_correct = True
            else:
                yellow_count += 1
        if yellow_correct:
            boxes = boxes + YELLOW_BOX
        else:
            boxes = boxes + WHITE_BOX
    letter_count += 1
# If user got the word right then give the winning statement vs if they did not get the word as them to try again
if guess == SECRET_WORD:
    print(boxes)
    print("Woo! You Got It!")
else:
    print(boxes)
    print("Not quite. Play again soon!")