from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

status = True
menu = Menu()
coffee_machine = CoffeeMaker()
money = MoneyMachine()

def check_choice(choice):
    while (not choice == 'espresso' and
           not choice == 'latte' and
           not choice =='cappuccino' and
           not choice == 'off' and
           not choice == 'report'):
        print("You didn't type the option correctly")
        choice = input(f"What would you like? ({menu.get_items()}):\n").lower()
    return choice

while status:
    choice = input(f"What would you like? ({menu.get_items()}):\n").lower()
    choice = check_choice(choice)
    if choice == 'off':
        status = False
    elif choice == 'report':
        coffee_machine.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)


