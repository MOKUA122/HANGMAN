import random

# List of hangman words
hangman_words = ['python', 'tuples', 'code', 'zindua', 'lists' 'isaac' 'dictionaries' 'school'] 

# Choose a random word from the list
word = random.choice(hangman_words)

# Create a list of dashes to represent the hidden word
hidden_word = ['_'] * len(word)

# Keep track of the number of failed attempts
failed_attempts = 0

# Keep track of the letters that have been guessed
guessed_letters = []

# Start the game
while '_' in hidden_word and failed_attempts < 6:
    print(' '.join(hidden_word))
    print('Guessed letters: ', guessed_letters)
    letter = input('Guess a letter: ')

    try:
        # Check if the input is a single letter
        if len(letter) != 1:
            print  ("ValueError")
        # Check if the letter has already been guessed
        elif letter in guessed_letters:
            print  ("ValueError")
    except ValueError:
        print('Invalid input. Please enter a single letter that has not been guessed before.')
        continue

    guessed_letters.append(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                hidden_word[i] = letter
    else:
        failed_attempts += 1
        print(f'Letter not in word. You have {6 - failed_attempts} attempts remaining.')

# Check if the player won or lost
if '_' not in hidden_word:
    print(' '.join(hidden_word))
    print('You won!')
else:
    print('You lost.')
    print('The word was:', word)
