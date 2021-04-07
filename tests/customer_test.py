import unittest
from src.customer import Customer 
from src.drink import Drink
from src.pub import Pub
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Steve", 20, 40, 7)

    def test_Customer_has_name(self):
        self.assertEqual("Steve", self.customer.name)

    def test_buy_drink(self):
        beer = Drink("Beer", 3, 4.5)
        food = Food("Chips", 2.50, 5)
        pub = Pub("The Prancing Pony", 100.00, ["beer", "cider"], food)
        self.customer.buy_drink(beer)
        self.assertEqual(17, self.customer.wallet)

    def test_can_customer_get_drunk(self):
        drink = Drink("Wine", 2.50, 4)
        self.customer.consume_drink(drink)
        self.assertEqual(11, self.customer.drunkeness)

    def test_buy_food(self):
        food = Food("Chips", 2.50, 5)
        pub = Pub("The Prancing Pony", 100.00, ["beer", "cider"], food)
        self.customer.buy_food(food)
        self.assertEqual(17.50, self.customer.wallet)

    def test_drunkeness_has_gone_down_after_eating_food(self):
        food = Food("Chips", 2.50, 5)
        self.customer.eat_food(food)
        self.assertEqual(2, self.customer.drunkeness)