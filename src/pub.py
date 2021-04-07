class Pub:

    def __init__(self, name: str, till: float, drinks: list):
        self.name =  name
        self.till = till
        self.drinks = []

    def add_till(self, price):
        self.till += price



