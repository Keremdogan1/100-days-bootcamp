from art import logo

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def getRandomCard(cards, deck, score):
    randomNumber = random.randint(0,12)
    if(cards[randomNumber] == 11 and score + cards[randomNumber] > 21):
        deck.append(cards[randomNumber] - 10)
    else:
        deck.append(cards[randomNumber])

def writeCurrent(userDeck, userScore, computerDeck):
    print(f"Your cards: {userDeck}, current score: {userScore}")
    print(f"Computer's first card = {computerDeck[0]}")

def writeFinal(userDeck, userScore, computerDeck, computerScore):
    print(f"Your final hand: {userDeck}, final score: {userScore}")
    print(f"Computer's final hand: {computerDeck}, final score: {computerScore}")



will_user_play = True

while will_user_play:
    userDeck = []
    userScore = 0

    computerDeck = []
    computerScore = 0

    print(logo)
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if choice == "y":
        will_user_play = True
    else:
        will_user_play = False
        break

    getRandomCard(cards, userDeck, userScore)
    getRandomCard(cards, userDeck, userScore)
    userScore = sum(userDeck)

    getRandomCard(cards, computerDeck, computerScore)
    getRandomCard(cards, computerDeck, computerScore)
    computerScore = sum(computerDeck)

    if userScore == 21 and computerScore < 21:
        writeCurrent(userDeck, userScore, computerDeck)
        writeFinal(userDeck, userScore, computerDeck, computerScore)
        print("You won with a blackjack 😎")

    elif userScore < 21 and computerScore == 21:
        writeCurrent(userDeck, userScore, computerDeck)
        writeFinal(userDeck, userScore, computerDeck, computerScore)
        print("Computer won with a blackjack 😱")

    elif userScore == 21 and computerScore == 21:
        writeCurrent(userDeck, userScore, computerDeck)
        writeFinal(userDeck, userScore, computerDeck, computerScore)
        print("Draw with both blackjacks, wow!")

    else:
        while(True):
            writeCurrent(userDeck, userScore, computerDeck)
            userChoice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if userChoice == "y":
                getRandomCard(cards, userDeck, userScore)
                userScore = sum(userDeck)
                if userScore > 21:
                    writeFinal(userDeck, userScore, computerDeck, computerScore)
                    print(f"You went over. You lost 😭")
                    break
            else:
                break

        while(computerScore <= 16):
            getRandomCard(cards, computerDeck, computerScore)
            computerScore = sum(computerDeck)
            if computerScore > 21:
                writeFinal(userDeck, userScore, computerDeck, computerScore)
                print(f"Computer went over. You won 😁")
                break

        if (21 >= userScore > computerScore):
            writeFinal(userDeck, userScore, computerDeck, computerScore)
            print(f"You won 😃")
            continue
        elif (userScore == computerScore and userScore <= 21):
            writeFinal(userDeck, userScore, computerDeck, computerScore)
            print(f"Draw 🙃")
            continue
        elif (21 >= computerScore > userScore):
            writeFinal(userDeck, userScore, computerDeck, computerScore)
            print(f"You lost 😤")
            continue
    print("\n" * 20)