import unittest
from src.drink import Drink 

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Beer", 3.70, 4.5)

    def test_Drink_has_name(self):
        self.assertEqual("Beer", self.drink.name)

    def test_Drink_has_alcohol_level(self):
        self.assertEqual(4.5, self.drink.alcohol_level)

