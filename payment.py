
class User:
    def __init__(self, username, email, password, firstName, lastName,confirm_password, phoneNumber):
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password=confirm_password
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        
                    
    def get_username(self):
        return self.username  
    
    def get_email(self):
        return self.email  
    
    def get_first_Name(self):
        return self.firstName  
    
    def get_lastName(self):
        return self.lastName 
    
    def phone_number(self):
        return self.phoneNumber
     
    def get_password(self):
        return self.password
    
user1 = User(username="Lisa",email="lisa@gmail.com",password=567892,firstName="Alicia",lastName="Njer",confirm_password=567892,phoneNumber="07654321")
username = user1.get_username()
print(username)
email = user1.get_email()
print(email)
firstname = user1.get_first_Name()
print(firstname)
lastName = user1.get_lastName()
print(lastName)
phoneNumber = user1.phone_number()
print(phoneNumber)
password = user1.get_password()
print(password)



class Product:
    def __init__(self,name,price,category,stock):
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock
        
        
class Order:
    def __init__(self, deliveryOptions,location,driver):
        self.location = location
        self.deliveryOptions = deliveryOptions
        self.driver = driver
        
class Payments:
    def __init__(self, order, method, amount):
        self.order = order
        self.method = method
        self.amount = amount

    def process_payment(self):
        print("Processing payment...")
        # Code to process payment here
        print("Payment processed successfully.")

    def view_info(self):
        print("Payment Details:")
        print(f"Amount: ${self.amount:.2f}")
        print(f"Method: {self.method}")

# Example objects
product1 = Product(name="Kales",price=35,category="vegetable",stock=200)
customer1 = User(username="Johnte",email="johnny@gmail.com",password=45677,firstName="Johnny",lastName="Mwangi",confirm_password=45677,phoneNumber="074536254")
order1 = Order(deliveryOptions="motorbike",location="Karen",driver="Mwangi Paul")

payment1 = Payments(order1, "Credit Card", 2.50)

payment1.view_info()

payment1.process_payment()
