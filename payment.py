class Payment:
    def __init__(self, amount, method, date, receipt, status, order):
        self.amount = amount
        self.method = method
        self.date = date
        self.receipt = receipt
        self.status = status
        self.order = order
    
    def verify_confirm(self):
        if self.method == "M_pesa":
            self.status = "verified"
        elif self.method == "Bank":
            self.status = "confirmed"
        elif self.method =="Cash":
            self.status = "Processed"        
        else:
            self.status = "unknown"

payment1 = Payment(amount=1000, method="M_pesa", date="2023-05-23", receipt="123456", status="pending", order="ABC123")
payment1.verify_confirm()

print(payment1.status)

        
        

            



            
