class Feedback:
    def __init__(self,customer,message):
        self.customer = customer
        self.message = message
    def display(self):
         print(self.message)
        # return f"{self.message}"


class Feedback:
    def __init__(self,customer,message):
        self.customer = customer
        self.message = message

    def display(self):
         return f"Hello {self.message}"


    def get_customer(self):
       return self.customer


    def get_message(self):
      return self.message

feedback1 = Feedback(customer="Alicia",message="Good work,i received my groceries")
feedback1.display()

feedback2 = Feedback(customer="Juana",message="I received my goods on time")



