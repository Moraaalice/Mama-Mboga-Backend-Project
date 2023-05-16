class Feedback:
    def __init__(self,customer,message):
        self.customer = customer
        self.message = message
    def display(self):
         print(self.message)
        # return f"{self.message}"


