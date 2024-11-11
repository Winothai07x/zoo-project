import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
       
    def test_ticket_price_invalid_age(self):
        self.assertEqual(self.zoo.get_ticket_price(-3), "Invalided")

    def test_ticket_price_child_boundary(self):
        self.assertEqual(self.zoo.get_ticket_price(10), 50)

    def test_ticket_price_teen(self):
        self.assertEqual(self.zoo.get_ticket_price(15), 100)

    def test_ticket_price_adult(self):
        self.assertEqual(self.zoo.get_ticket_price(40), 150)

    def test_ticket_price_senior(self):
        self.assertEqual(self.zoo.get_ticket_price(70), 100)


if __name__ == '__main__':
    unittest.main()
