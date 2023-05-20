#cart
class Cart:
    def __init__(self, item, phone_number, payment,address):
        self.name = item
        self.phone_number = phone_number
        self.payment = payment
        self.address = address
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)

    def remove_from_cart(self, item):
        if item in self.cart:
            self.cart.remove(item)

    def view_cart(self):
        if len(self.cart) == 0:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for item in self.cart:  
                    print("- " + item)

# Example objects
customer1 = Cart(item="Mangoes",phone_number="0765433289",payment="cash on delivery",address=56788)

# Example usage
customer1.add_to_cart("Apples")
customer1.add_to_cart("Bananas")
customer1.view_cart()
