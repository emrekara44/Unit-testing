import unittest
from cart import ShoppingCart

class TestShoppingCartSystem(unittest.TestCase):
    def test_full_system_lifecycle(self):
        cart = ShoppingCart()
        cart.add_item("Book", 10, 3)
        cart.set_shipping_fee(5)
        cart.apply_discount(10)
        self.assertEqual(cart.total_price(), 32)
        cart.clear()
        self.assertEqual(len(cart.items), 0)
        self.assertEqual(cart.total_price(), 0)

if __name__ == "__main__":
    unittest.main()
