import random

from art import logo
print(logo)

selected_number = random.randint(1,100)
health = 0
guess = 0

print()
print("Welcome to the Number Guessing Game!")
print("I'm thinking a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    health = 10
else:
    health = 5

while guess != selected_number and health > 0 :
    print(f"You have {health} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > selected_number:
        print("Too high.\nGuess again")
        health -= 1
    elif guess < selected_number:
        print("Too low.\nGuess again")
        health -= 1

if health > 0:
    print(f"You got it! The answer was {selected_number}.")
else:
    print(f"You've run out of guesses, the number was {selected_number}.\nTry again!")