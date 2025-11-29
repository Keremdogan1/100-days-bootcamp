from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker_object = CoffeeMaker()
money_machine_object = MoneyMachine()
menu_object = Menu()

def work():
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if prompt == "off":
        return 0

    elif prompt == "report":
        coffee_maker_object.report()
        money_machine_object.report()

    elif prompt == "espresso" or prompt == "latte" or prompt == "cappuccino":
        menu_item_object = menu_object.find_drink(prompt)

        if coffee_maker_object.is_resource_sufficient(menu_item_object):
            if money_machine_object.make_payment(menu_item_object.cost):
                coffee_maker_object.make_coffee(menu_item_object)
    else:
        print("Invalid input, try again.")
    work()

work()