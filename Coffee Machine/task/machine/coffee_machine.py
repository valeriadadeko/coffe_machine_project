class CoffeeMachine:
    WATER_FOR_ONE_CUP = 200
    MILK_FOR_ONE_CUP = 50
    BEANS_FOR_ONE_CUP = 15
    ESPRESSO_COFFEE_TYPE = 1
    LATTE_COFFEE_TYPE = 2
    CAPPUCCINO_COFFEE_TYPE = 3
    ACTION_BUY = 'buy'
    ACTION_TAKE = 'take'
    ACTION_FILL = 'fill'
    ACTION_FILL_BEANS = 'beans'
    ACTION_FILL_WATER = 'water'
    ACTION_FILL_MILK = 'milk'
    ACTION_FILL_CUPS = 'cups'
    ACTION_REMAINING = 'remaining'
    ACTION_EXIT = 'exit'
    ACTION_BACK = 'back'

    def __init__(self):
        self.current_water = 400
        self.current_milk = 540
        self.current_beans = 120
        self.current_disposable_cups = 9
        self.current_amount_of_money = 550
        self.current_state = None

    def print_coffee_machine_state(self):
        print('The coffee machine has:')
        print('{} of water'.format(self.current_water))
        print('{} of milk'.format(self.current_milk))
        print('{} of coffee beans'.format(self.current_beans))
        print('{} of disposable cups'.format(self.current_disposable_cups))
        print('$ {} of money'.format(self.current_amount_of_money))

    def check_water(self, water_for_coffee):
        if self.current_water - water_for_coffee < 0:
            print('Sorry, not enough water!')
            return False
        else:
            return True

    def check_cups(self):
        if self.current_disposable_cups <= 0:
            print('Sorry, not enough disposable cups!')
            return False
        else:
            return True

    def check_milk(self, milk_for_coffee):
        if self.current_milk - milk_for_coffee < 0:
            print('Sorry, not enough milk!')
            return False
        else:
            return True

    def check_beans(self, beans_for_coffee):
        if self.current_beans - beans_for_coffee < 0:
            print('Sorry, not enough beans!')
            return False
        else:
            return True

    def prepare_coffee(self, coffee_type):
        if not self.check_cups():
            return

        if coffee_type == CoffeeMachine.ESPRESSO_COFFEE_TYPE:
            if self.check_beans(16) and self.check_water(250):
                self.current_water -= 250
                self.current_beans -= 16
                self.current_disposable_cups -= 1
                self.current_amount_of_money += 4
                print('I have enough resources, making you a coffee!')
        elif coffee_type == CoffeeMachine.LATTE_COFFEE_TYPE:
            if self.check_water(350) and self.check_beans(20) and self.check_milk(75):
                self.current_water -= 350
                self.current_milk -= 75
                self.current_beans -= 20
                self.current_disposable_cups -= 1
                self.current_amount_of_money += 7
                print('I have enough resources, making you a coffee!')
        elif coffee_type == CoffeeMachine.CAPPUCCINO_COFFEE_TYPE:
            if self.check_water(20) and self.check_beans(12) and self.check_milk(100):
                self.current_water -= 200
                self.current_milk -= 100
                self.current_beans -= 12
                self.current_disposable_cups -= 1
                self.current_amount_of_money += 6
                print('I have enough resources, making you a coffee!')

    def get_money_from_coffee_machine(self):
        print('I gave you ' + str(self.current_amount_of_money))
        self.current_amount_of_money = 0

    def fill_coffee_machine(self, water, milk, beans, cups):
        self.current_water += water
        self.current_milk += milk
        self.current_beans += beans
        self.current_disposable_cups += cups

    def read_user_input(self, user_input):
        if self.current_state is not None:
            if user_input == CoffeeMachine.ACTION_BACK:
                self.current_state = None
            elif self.current_state == CoffeeMachine.ACTION_BUY:
                self.prepare_coffee(int(user_input))
                self.current_state = None
            elif self.current_state == CoffeeMachine.ACTION_FILL_WATER:
                self.current_water += int(user_input)
                self.current_state = CoffeeMachine.ACTION_FILL_MILK
            elif self.current_state == CoffeeMachine.ACTION_FILL_MILK:
                self.current_milk += int(user_input)
                self.current_state = CoffeeMachine.ACTION_FILL_BEANS
            elif self.current_state == CoffeeMachine.ACTION_FILL_BEANS:
                self.current_beans += int(user_input)
                self.current_state = CoffeeMachine.ACTION_FILL_CUPS
            elif self.current_state == CoffeeMachine.ACTION_FILL_CUPS:
                self.current_disposable_cups += int(user_input)
                self.current_state = None
        elif user_input == CoffeeMachine.ACTION_BUY:
            self.current_state = CoffeeMachine.ACTION_BUY
        elif user_input == CoffeeMachine.ACTION_FILL:
            self.current_state = CoffeeMachine.ACTION_FILL_WATER
        elif user_input == CoffeeMachine.ACTION_TAKE:
            self.get_money_from_coffee_machine()
        elif user_input == CoffeeMachine.ACTION_REMAINING:
            self.print_coffee_machine_state()

    def __repr__(self):
        return 'current state of coffee machine: {}'.format(self.current_state)


coffee_machine = CoffeeMachine()

while True:
    action = str(input('Write action (buy, fill, take, remaining, exit):'))
    if action == CoffeeMachine.ACTION_EXIT:
        break
    if action == CoffeeMachine.ACTION_BUY:
        coffee_machine.read_user_input(action)
        coffee_type_input = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to '
                                  'main menu:')
        coffee_machine.read_user_input(coffee_type_input)
    elif action == CoffeeMachine.ACTION_FILL:
        coffee_machine.read_user_input(CoffeeMachine.ACTION_FILL)
        coffee_machine.read_user_input(input('Write how many ml of water do you want to add:'))
        coffee_machine.read_user_input(input('Write how many ml of milk do you want to add:'))
        coffee_machine.read_user_input(input('Write how many grams of coffee beans do you want to add:'))
        coffee_machine.read_user_input(input('Write how many disposable cups of coffee do you want to add:'))
    else:
        coffee_machine.read_user_input(action)
