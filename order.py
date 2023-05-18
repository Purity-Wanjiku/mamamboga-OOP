class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Product:
    def __init__(self, name, product_type, availability, price, description):
        self.name = name
        self.product_type = product_type
        self.availability = availability
        self.price = price
        self.description = description
    
    def update_availability(self, availability):
        self.availability = availability
    
    def update_price(self, price):
        self.price = price
    
    def update_description(self, description):
        self.description = description

class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

class Order:
    def __init__(self, user, items):
        self.user = user
        self.items = items
    
    def total_cost(self):
        total = 0
        for item in self.items:
            total += item.product.price * item.quantity
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
product1 = Product('apple', 'fruit', 10, 1.0, 'A juicy fruit with a crisp texture.')
product2 = Product('carrot', 'vegetable', 5, 0.5, 'A root vegetable with a crunchy texture.')
item1 = OrderItem(product1, 3)
item2 = OrderItem(product2, 2)
order_manager = OrderManager()
order = order_manager.place_order(user, [item1, item2])
print(f'Order placed with total cost: ${order.total_cost()}')