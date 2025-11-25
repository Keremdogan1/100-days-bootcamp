game_level = 3
enemies = ["Skeleton","Zombie","Alien"]


def create_enemy():
    new_enemy = ""
    if game_level < 5 :
        new_enemy = enemies[0]

    print(new_enemy) # You can access inside of if statements/while loops/for loops from global scope