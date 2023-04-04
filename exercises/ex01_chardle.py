"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730562389"

# Input for 5 letter word and Error command
wordle_word: str = input("Enter a 5-character word: ")
if (len(wordle_word) != 5):
    print("Error: Word must contain 5 characters")
    exit()

# Variables
single_char: str = input("Enter a single character: ")
index_val: int = 0
lettercount: int = 0

# Error command for single character
if (len(single_char) != 1):
    print("Error: Character must be a single character.")
    exit()

# Print command for once both 5-character word and single character have been inputed
print("Searching for " + single_char + " in " + wordle_word)

# Index values and letter count
if (single_char == wordle_word[index_val]):
    print(single_char + " found at index " + str(index_val))
    lettercount += 1
index_val = index_val + 1

if (single_char == wordle_word[index_val]):
    print(single_char + " found at index " + str(index_val))
    lettercount += 1
index_val = index_val + 1

if (single_char == wordle_word[index_val]):
    print(single_char + " found at index " + str(index_val))
    lettercount += 1
index_val = index_val + 1

if (single_char == wordle_word[index_val]):
    print(single_char + " found at index " + str(index_val))
    lettercount += 1
index_val = index_val + 1

if (single_char == wordle_word[index_val]):
    print(single_char + " found at index " + str(index_val))
    lettercount += 1

# Final print statements depending on letter count
if (lettercount > 1):
    print(str(lettercount) + " instances of " + single_char + " found in " + wordle_word)

if (lettercount == 1):
    print(str(lettercount) + " instance of " + single_char + " found in " + wordle_word)

if (lettercount == 0):
    print("No instances of " + single_char + " found in " + wordle_word)