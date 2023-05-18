class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Product:
    def __init__(self, name, category, minimum-quantity, price):
        self.name = name
        self.category = category
        self.minimum-quantity = minimum-quantity
        self.price = price
    
    def update_name = (self,name):
        self.name = name
        
    def update_availability(self, category):
        self.category = category
    
    def update_price(self, price):
        self.price = price
    
    def update_minimum-quantity(self, minimum-quantity):
        self.minimum-quantity = minimum-quantity

class OrderItem:
    def __init__(self, product, minimum-quantity):
        self.product = product
        self.minimum-quantity = minimum-quantity

class Order:
    def __init__(self, user, items):
        self.user = user
        self.items = items
    
    def total_cost(self):
        total = 0
        for item in self.items:
            total += item.product.price * item.minimum-quantity
        return total

class OrderManager:
    def __init__(self):
        self.orders = []
    
    def place_order(self, user, items):
        order = Order(user, items)
        self.orders.append(order)
        return order

# Example usage:
user = User('val_buraje', 'password123')
product1 = Product('apple', 'fruit', 35, 250)
product2 = Product('carrot', 'vegetable', 105, 500)
item1 = OrderItem(product1, 3)
item2 = OrderItem(product2, 2)
order_manager = OrderManager()
order = order_manager.place_order(user, [item1, item2])
print(f'Order placed with total cost: ${order.total_cost()}')
