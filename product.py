   #   Category
class category:
     def __init__(self,name):
        self.name=name
     def add_category(self,new_name):
        self.name=new_name
     def __str__(self):
       return f"{self.name}"
# product
class product:
    def __init__(self,name,quantity,price):
        self.name=name
        self.quantity=quantity
        self.price=price
    def product_name(self,p_name):
        self.name=p_name
    def product_quantity(self,p_quantity):
        self.quantity=p_quantity
    def product_price(self,p_price):
        self.price=p_price
    def __str__(self):
        return f"{self.name},{self.quantity},{self.price}"
