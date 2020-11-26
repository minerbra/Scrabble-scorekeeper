"""

@Author: Brady Miner

This program will calculate the score of Scrabble words from a file.


"""

print("\nThis program will read words from a file, convert them to uppercase, and score each letter for Scrabble.\n"
      "\nInvalid characters will not be scored\n"
      "If the word has 0 letters or 10 letters or more, zero points are awarded.\n")

# Dictionary the get the point value for each letter

letter_score = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4,
                "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1,
                "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1,
                "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8,
                "Y": 4, "Z": 10}

word_scores = {}  # Store the words and score in a dictionary

with open('1030 Project 04 01 Words.txt') as f:  # Open and close file

    lines = f.readlines()  # Read file content line by line

    for word in lines:  # loop through the words and capitalize all letters
        word = word.strip().upper()  # Strip and convert letter to uppercase
        word_score = 0  # Counter for word score

        for letter in word:  # Loop letters in words from file
            if letter not in letter_score:  # if character not in dict assign zero points
                word_score += 0
            elif len(word) >= 10 or len(word) == 0:  # If length of word is zero or greater than 10 assign zero points
                word_score += 0
            else:  # Score each letter from dictionary
                word_score += letter_score.get(letter)

            word_scores[word] = word_score  # Add word score

print("Scorecard:\n")  # Output for Scrabble scorecard
for alpha, num in word_scores.items():
    print("{} = [{}] points".format(alpha, num))
