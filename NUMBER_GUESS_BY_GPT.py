import random

#thhis will select any number between 1 to 100
number_to_guess = random.randint(1,100)

#this will keep track for your attempts 
attempts = 0
while True:
    guess = int(input("Guess the number (1-100): "))
    attempts += 1
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")

    else:
        print(f"Congratulations! you guessed the number {number_to_guess} in {attempts} attempts.")
