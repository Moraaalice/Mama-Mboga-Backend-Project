class Order:
    def __init__(self, deliveryOptions):
        self.deliveryOptions = deliveryOptions
    def getDeliveryOptions(self):
        return self.deliveryOptions
order = Order( [ "Home Delivery", "Pickup point"])
deliveryOptions = order.getDeliveryOptions()
print(deliveryOptions)