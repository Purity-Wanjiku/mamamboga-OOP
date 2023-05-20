class Orders:
    def __init__(self, name, order, payment, delivery_address):
        self.order = order
        self.name = name
        self.payment = payment
        self.delivery_address = delivery_address
        
    def add_order(self):
        orders_dict = {
           "name": self.name,
           "order": self.order,
           "payment": self.payment,
           "delivery_address": self.delivery_address,
       }
        return orders_dict
    
# Example usage:
name = input("Input your name: ")
order = input("Input the type of order: ")
payment = input("Input the type of payment: ")
delivery_address = input("Input your delivery address: ")

new_order = Orders(name, order, payment, delivery_address)
print(new_order.add_order())


