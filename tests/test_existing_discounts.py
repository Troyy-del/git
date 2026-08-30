import unittest

from pricing import get_discount_rate


class ExistingDiscountTests(unittest.TestCase):
    def test_existing_customer_discounts(self) -> None:
        self.assertEqual(get_discount_rate("standard"), 0.05)
        self.assertEqual(get_discount_rate("premium"), 0.10)


if __name__ == "__main__":
    unittest.main()
