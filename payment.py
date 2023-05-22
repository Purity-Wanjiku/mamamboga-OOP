class Payment:
    def __init__(self, amount, payment_method, date, receipt):
        self.amount = amount
        self.payment_method = payment_method
        self.date = date
        self.receipt = receipt
        
    
    def process_payment(self):
        if self.payment_method == "mpesa":
            print(f"Processing payment of KES {self.amount:.2f} using Mpesa on {self.date}...")
            print(f"Mpesa confirmation code: {self.receipt}")
        elif self.payment_method == "cash":
            print(f"Received cash payment of KES {self.amount:.2f} on {self.date}.")
            print(f"Receipt number: {self.receipt}")
    
    def validate_payment(self):
        if self.payment_method == "mpesa":
            print("Mpesa payment details are valid")
        elif self.payment_method == "cash":
            print("Cash payment received")


# Example usage:
amount = float(input("Enter amount to be paid: "))
payment_method = input("Enter payment method (mpesa, cash): ")
date = input("Enter date of payment (DD/MM/YYYY): ")
receipt = input("Enter payment receipt number: ")

new_payment = Payment(amount, payment_method, date, receipt)

new_payment.validate_payment()
new_payment.process_payment()

