import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Chips", 2.50, 5)

    def test_Food_has_name(self):
        self.assertEqual("Chips", self.food.name)

    def test_Food_has_rejuvenation_level(self):
        self.assertEqual(5, self.food.rejuvenation_level)

