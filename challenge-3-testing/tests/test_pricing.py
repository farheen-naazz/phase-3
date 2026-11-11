import unittest
from pricing import calculate_final_price


class TestPricing(unittest.TestCase):

    def test_ten_percent_discount(self):
        self.assertEqual(calculate_final_price(200, 10), 180)

    def test_twenty_five_percent_discount(self):
        self.assertEqual(calculate_final_price(80, 25), 60)

    def test_zero_discount(self):
        self.assertEqual(calculate_final_price(200, 0), 200)

    def test_full_discount(self):
        self.assertEqual(calculate_final_price(100, 100), 0)

    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            calculate_final_price(200, 120)


if __name__ == "__main__":
    unittest.main()