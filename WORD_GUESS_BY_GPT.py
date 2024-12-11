#This code is used to create a game which will guess the word chosen by code randomly from specified list of options.

import random

#step-1 create a function that will provide list of options from which the word will ebe selected by code randomly 
def choose_random_word():
    word_list = ["apple", "banana", "cherry", "orange", "grape", "kiwi", "melon", "strawberry", "blueberry", "pineapple"]
    return random.choice(word_list)


#step-2 create a function that will display the correct word guessed by you
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

#step-3 create a function that will start the game and also provide the max_attempts that you can guess
def play_game():
    print("Welcome to 'Word Guess'!")
    secret_word = choose_random_word()
    guessed_letters = []
    max_attempts = 6

    while max_attempts > 0:
        display = display_word(secret_word, guessed_letters)
        print(display)
        guess = input("Guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter.")
            elif guess in secret_word:
                guessed_letters.append(guess)
                if secret_word == display_word(secret_word, guessed_letters):
                    print(f"Congratulations! You guessed the word '{secret_word}'!")
                    break
            else:
                guessed_letters.append(guess)
                max_attempts -= 1
                print(f"Wrong guess! You have {max_attempts} attempts left.")
        else:
            print("Invalid input. Please enter a single letter.")

    if max_attempts == 0:
        print(f"Game over! The word was '{secret_word}'.")

if __name__ == "__main__":
    play_game()






































