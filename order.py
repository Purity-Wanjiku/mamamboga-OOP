#Order class
class Order:
    def __init__(self, products_ordered, quantity, total_price, payment_method, order_status):
        self.products_ordered = products_ordered
        self.quantity = quantity
        self.total_price = total_price
        self.payment_method = payment_method
        self.order_status = order_status
    def update_order_status(self, new_order_status):
        self.order_status = new_order_status
    def __str__(self):
        return f"{self.products_ordered}, {self.quantity} ,{self.total_price},{self.payment_method} ,{self.order_status}"