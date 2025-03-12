from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


game_on = True

while game_on:
    res = input(f"What would you like ?({menu.get_items()}) \n")
    if res == "report":
        coffee_maker.report()
        money_machine.report()
    if not menu.find_drink(res):
        continue
    menu_item = None
    for item in menu.menu:
        if item.name == res:
            menu_item = item

    if not coffee_maker.is_resource_sufficient(menu_item):
        continue
    # money_machine.process_coins()
    cost = None
    for menu_item in menu.menu:
        if menu_item.name == res:
            cost = menu_item.cost
    money_machine.make_payment(cost)
    coffee_maker.make_coffee(menu_item)








