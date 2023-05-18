class Orders:
    def __init__(self,name,order,payment,deliveryAdress) :
        self.order=order
        self.name=name
        self.payment=payment
        self.deliveryAddress=deliveryAdress
        
        # dictionary of the order attribute 
    def add_order(self):
        orders_dict={
           "name":self.name,
           "order":self.order,
           "payment":self.payment,
           "deliveryAdress":self.deliveryAddress,
          
       }
        return orders_dict
    
    # instructs user to input their details
name=input("Input your name")
order=input("Input the type of order")
payment=input("Input the type of payment")
deliveryAddress=input("Input your delivery address")

    # User example
new_Customer=Orders(Name,order,payment,deliveryAddress)
user=new_Customer
print(new_Customer.add_order())
        order = Order(user, items)
        self.orders.append(order)
        return order


