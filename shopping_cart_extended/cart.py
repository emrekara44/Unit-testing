class ShoppingCart:
    def __init__(self):
        self.items = {}  # ürün_adı: (fiyat, adet)
        self.discount_rate = 0
        self.coupons = {}  # kupon_kodu: indirim_oranı
        self.shipping_fee = 0.0

    def add_item(self, name, price, quantity=1):
        if name in self.items:
            current_price, current_quantity = self.items[name]
            self.items[name] = (price, current_quantity + quantity)
        else:
            self.items[name] = (price, quantity)

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def update_quantity(self, name, quantity):
        if name in self.items:
            price, _ = self.items[name]
            self.items[name] = (price, quantity)

    def apply_discount(self, percentage):
        if 0 <= percentage <= 100:
            self.discount_rate = percentage
        else:
            raise ValueError("Discount must be between 0 and 100.")

    def add_coupon(self, code, discount_percent):
        if 0 <= discount_percent <= 100:
            self.coupons[code] = discount_percent

    def apply_coupon(self, code):
        if code in self.coupons:
            self.apply_discount(self.coupons[code])
        else:
            raise ValueError("Invalid coupon code.")

    def set_shipping_fee(self, fee):
        self.shipping_fee = fee

    def total_price(self):
        subtotal = sum(price * quantity for price, quantity in self.items.values())
        discount = subtotal * (self.discount_rate / 100)
        return round(subtotal - discount + self.shipping_fee, 2)

    def clear(self):
        self.items = {}
        self.discount_rate = 0
        self.shipping_fee = 0.0
