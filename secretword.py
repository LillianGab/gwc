# import random

# # A list of words that 
# potential_words = ["example", "words", "someone", "can", "guess"]

# word = random.choice(potential_words)

secret_word = "hydration"
# Use to test your code:
# print(word)

# Converts the word to lowercase
secret_word = secret_word.lower()

# Make it a list of letters for someone to guess
current_word = ["h", "y", "d", "r", "a", "t", "i", "o", "n"] # TIP: the number of letters should match the word

# Some useful variables
guesses = []
maxfails = 9
fails = 0

while fails < maxfails:
    guess = input("Guess a letter: ")
    guesses.append(guess)
    print(guesses in secret_word)
	# check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!

print(current_word)

fails = fails+1
print("You have " + str(maxfails - fails) + " tries left!")





    # assign some secret word that user must guess
    # use list to store word, example: ["a", "b", "_"]
    # have some variable which tells us if the game keeps going and to continue the while loop
    # store user's guess to see if letter in word
        # ask user to guess letter
        # if user's guess is in the word, fill in the list according to where the letter is in the word
        # if user's guess is NOT in the word, ask again. Do not update the list. (while loop)

secret_word = "hydration"
current_word = ["h", "y", "d", "r", "a", "t", "i", "o", "n"]
guesses = []
maxfails = 9
fails = 0

while fails < maxfails:
    guess = input("Guess a letter: ")
    guesses.append(guess)
    print(guesses in secret_word)

    print(current_word)

fails = fails+1
print("You have " + str(maxfails - fails) + " tries left!")




