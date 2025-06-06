import unittest
from cart import ShoppingCart

class TestShoppingCartIntegration(unittest.TestCase):
    def test_checkout_flow_with_coupon_and_shipping(self):
        cart = ShoppingCart()
        cart.add_item("Laptop", 1500, 1)
        cart.add_item("Mouse", 50, 2)
        cart.add_coupon("SUMMER10", 10)
        cart.apply_coupon("SUMMER10")
        cart.set_shipping_fee(20)
        self.assertEqual(cart.total_price(), 1460)

    def test_update_and_remove_items(self):
        cart = ShoppingCart()
        cart.add_item("Phone", 1000, 1)
        cart.add_item("Case", 20, 1)
        cart.update_quantity("Phone", 2)
        cart.remove_item("Case")
        self.assertEqual(cart.total_price(), 2000)

if __name__ == "__main__":
    unittest.main()
