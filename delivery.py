class Order:
    def __init__(self, deliveryOptions,location,driver):
        self.deliveryOptions = deliveryOptions
        self.location = location
        self.driver = driver
        products=[]
        
    def add_product(self, productName, productPrice):
        self.products.append((productName, productPrice))
    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product[1]
        return total
    
    def removeProduct(self, product):
        self.products.remove(product)
        
    def getDeliveryOptions(self):
        return self.deliveryOptions 
      
 order = Order(deliveryOptions, location, driver)
order.add_product("Product 1", 10.99)
order.add_product("Product 2", 5.99)

total = order.calculate_total()
print("Total: $", total)

order.removeProduct(("Product 1", 10.99)) options = order.getDeliveryOptions()
print("Delivery options:", options)

