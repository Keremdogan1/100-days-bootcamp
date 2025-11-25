# Modifying Global Scope

enemies = 1


def increase_enemies(enemies):
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies(enemies)
print(f"enemies outside function: {enemies}")


