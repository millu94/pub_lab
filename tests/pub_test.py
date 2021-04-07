import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00, ["beer", "cider"])

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_till_cash(self):
        self.assertEqual(100.00 ,self.pub.till)

    # def test_sell_drink(self):
    #     drink = Drink("Tennents", 2.50)
    #     self.pub.sell_drink(drink)
    #     self.assertEqual(102.50, self.pub.till)

    def test_sell_drink_legal(self):
        drink = Drink("Tennents", 2.50)
        customer = Customer("Jimmy", 30, 21, 1)
        self.pub.sell_drink(drink, customer)
        self.assertEqual(102.50, self.pub.till)

    def test_sell_drink_illegal(self):
        drink = Drink("Tennents", 2.50)
        customer = Customer("Jimmy", 30, 17, 0)
        self.pub.sell_drink(drink, customer)
        self.assertEqual(100.00, self.pub.till)

    def test_sell_drink_if_not_drunk(self):
        drink = Drink("Tennents", 2.50)
        customer = Customer("Gregg", 30, 26, 0)
        self.pub.sell_drink(drink, customer)
        self.assertEqual(102.50, self.pub.till) 

    def test_sell_drink_if_drunk(self):
        drink = Drink("Tennents", 2.50)
        customer = Customer("Gregg", 30, 26, 10)
        self.pub.sell_drink(drink, customer)
        self.assertEqual(100.00, self.pub.till)    