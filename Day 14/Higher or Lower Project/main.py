import random
from game_data import data
from art import vs
from art import logo

def select_famous(data_list):
    index = random.randint(0 , len(data_list) - 1)
    selected = data_list[index]
    data.remove(data_list[index])
    return selected


def game():
    data_copy = data
    score = 0
    print(logo)
    a = select_famous(data_copy)

    while len(data_copy):
        b = select_famous(data_copy)

        print(f"Compare A: {a['name']}, a/an {a['description']}, from {a['country']}.")
        print(vs)
        print(f"Against B: {b['name']}, a/an {b['description']}, from {b['country']}.")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        try:
            if guess == "a" :
                if a['follower_count'] >= b['follower_count']:
                    print("\n" * 20)
                    score += 1
                    print(logo)
                    print(f"You're right! Current score: {score}.")
                    a = b
                else:
                    print("\n" * 20)
                    print(logo)
                    print(f"Sorry, that's wrong. Final score: {score}.")
                    return 0
            elif guess == "b" :
                if b['follower_count'] >= a['follower_count']:
                    score += 1
                    print("\n" * 20)
                    print(logo)
                    print(f"You're right! Current score: {score}.")
                    a = b
                else:
                    print("\n" * 20)
                    print(logo)
                    print(f"Sorry, that's wrong. Final score: {score}.")
                    return 0
            else:
                print("\n" * 20)
                print(logo)
                input("Not a valid input try again! (Press enter key to continue) ")
                print("\n" * 20)
                game()
        except TypeError:
            print("\n" * 20)
            print(logo)
            input("Not a valid input try again! (Press enter key to continue) ")
            print("\n" * 20)
            game()

    print("Wow you compared the whole famous list correctly!")
    return 1

game()
