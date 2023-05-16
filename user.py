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