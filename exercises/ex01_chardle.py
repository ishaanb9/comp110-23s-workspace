"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730562389"

wordle_word: str = input("Enter a 5 character word: ")
if (len(wordle_word) != 5):
    print("Error: Word must contain 5 characters")

single_char: str = input("Enter a single character: ")
index_val: int = 0
lettercount: int = 0

if (len(single_char) != 1):
    print("Error: Character must be a single character.")
  
print("Searching for " + single_char + " in " + wordle_word)

if(single_char == wordle_word[index_val]):
    print(single_char + " found at " + str(index_val))
    lettercount += 1
index_val = index_val + 1

if(single_char == wordle_word[index_val]):
    print(single_char + " found at " + str(index_val))
    lettercount += 1
index_val = index_val + 1

if(single_char == wordle_word[index_val]):
    print(single_char + " found at " + str(index_val))
    lettercount += 1
index_val = index_val + 1

if(single_char == wordle_word[index_val]):
    print(single_char + " found at " + str(index_val))
    lettercount += 1

print(str(lettercount) + " instances of " + single_char + " found in " + wordle_word)



