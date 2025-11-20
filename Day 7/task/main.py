
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
    # TODO-6: - Update the code below to tell the user how many lives they have left.
    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.
            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py

import random
from soupsieve.util import lower
from hangman_art import stages, logo
from hangman_words import word_list


random_index = random.randint(0, len(word_list) - 1)
chosen_word = word_list[random_index]
chosen_word_len = len(chosen_word)

hide =["_"] * chosen_word_len

live = 6
chosed_true_letters = []

print(logo)

while(live):
    str_hide = "".join(hide)
    print(f"Word to guess:{str_hide}")
    player_letter = lower(input("Guess a letter: "))

    if player_letter in chosed_true_letters:
        print(f"You've already guessed {player_letter}")

    elif player_letter in chosen_word:
        chosed_true_letters.append(player_letter)
        for index in range(len(chosen_word)):
            if chosen_word[index] == player_letter:
                hide[index] = player_letter

    else:
        print(f"You guessed {player_letter}, that's not in the word. You lose a life.")
        live -= 1
    print("".join(hide))
    print(stages[live - 1])
    if live and "_" in hide:
        print(f"****************************{live}/6 LIVES LEFT****************************")
    if not "_" in hide:
        print(f"****************************It was {chosen_word}! YOU WIN****************************")
        break

if not live: print(f"****************************It was {chosen_word}! YOU LOST****************************")
