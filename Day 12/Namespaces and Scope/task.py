enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

def game():
    health = 10
    def drink_posion():
        posion_power = 2
        print(health)

    drink_posion()

game()
