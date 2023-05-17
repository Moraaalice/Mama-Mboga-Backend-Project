class Order:
    def __init__(self, deliveryOptions):
        self.deliveryOptions = deliveryOptions
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
      
 

            
    
    
    
    
    
order = Order( [ "Home Delivery", "Pickup point"])
deliveryOptions = order.getDeliveryOptions()
print(deliveryOptions)
