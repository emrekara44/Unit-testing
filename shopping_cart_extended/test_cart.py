import unittest
from cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_and_total(self):
        self.cart.add_item("Laptop", 1500, 1)
        self.cart.add_item("Mouse", 50, 2)
        self.assertEqual(self.cart.total_price(), 1600)

    def test_update_quantity(self):
        self.cart.add_item("Monitor", 300, 1)
        self.cart.update_quantity("Monitor", 2)
        self.assertEqual(self.cart.items["Monitor"], (300, 2))

    def test_apply_discount(self):
        self.cart.add_item("Chair", 200, 1)
        self.cart.apply_discount(10)
        self.assertEqual(self.cart.total_price(), 180)

    def test_add_and_apply_coupon(self):
        self.cart.add_item("Table", 500, 1)
        self.cart.add_coupon("SAVE20", 20)
        self.cart.apply_coupon("SAVE20")
        self.assertEqual(self.cart.total_price(), 400)

    def test_invalid_coupon(self):
        with self.assertRaises(ValueError):
            self.cart.apply_coupon("INVALID")

    def test_shipping_fee(self):
        self.cart.add_item("Phone", 1000, 1)
        self.cart.set_shipping_fee(15)
        self.assertEqual(self.cart.total_price(), 1015)

    def test_clear_cart(self):
        self.cart.add_item("Book", 20, 2)
        self.cart.clear()
        self.assertEqual(len(self.cart.items), 0)
        self.assertEqual(self.cart.total_price(), 0)

    def test_failing_case(self):
        self.cart.add_item("Pen", 5, 2)
        self.cart.apply_discount(10)
        # Verify discounted total after applying 10% discount to two pens
        self.assertEqual(self.cart.total_price(), 9)

if __name__ == "__main__":
    unittest.main()
