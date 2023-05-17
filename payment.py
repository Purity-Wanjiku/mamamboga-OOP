class category:
     def __init__(self,name,phone_number,amount):
        self.name=name
        self.phone_number=phone_number
        self.amount=amount
     def __str__(self):
        return f"{self.name},{self.phone_number},{self.amount}"