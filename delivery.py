class Order:
    def __init__(self, deliveryOptions):
        self.deliveryOptions = deliveryOptions
    def getDeliveryOptions(self):
        return self.deliveryOptions
    def calculate_total(product_price):
        sum=0
        for price in product_price:
            sum+=price
            
    
    
    
    
    
order = Order( [ "Home Delivery", "Pickup point"])
deliveryOptions = order.getDeliveryOptions()
print(deliveryOptions)
