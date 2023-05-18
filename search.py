class Product:
    def __init__(self, name, available):
        self.name = name
        self.available = available
    
    def check_availability(self):
        if self.available:
            return f"The {self.name} is available."
        else:
            return f"Sorry, the {self.name} is not available."

class ProductManager:
    def __init__(self):
        self.products = []
    
    def add_product(self, name, available):
        product = Product(name, available)
        self.products.append(product)
    
    def search_product(self, name):
        for product in self.products:
            if product.name == name:
                return product.check_availability()
        return f"Sorry, the {name} is not found ."

