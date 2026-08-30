import unittest

from pricing import get_discount_rate


class VipDiscountTests(unittest.TestCase):
    def test_vip_customer_discount(self) -> None:
        self.assertEqual(get_discount_rate("vip"), 0.20)


if __name__ == "__main__":
    unittest.main()
