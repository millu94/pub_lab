class Pub:

    def __init__(self, name: str, till: float, drinks: list, food):
        self.name =  name
        self.till = till
        self.drinks = []
        self.food = []

    def sell_drink(self, drink, customer):
        if (customer.age >= 18) & (customer.drunkeness <= 6):
            self.till += drink.price

    



