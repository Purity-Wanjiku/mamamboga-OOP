class Product:
    def __init__(self, name, availability):
        self.name = name
        self.availability = availability
    def check_availability(self):
        if self.availability:
            return f"The {self.name} is available."
        else:
            return f"Sorry, the {self.name} is not available."
my_object = Product("Tomoko",False)
print (my_object.check_availability())
my_object = Product("Guava",True)
print (my_object.check_availability())
class ProductManager:
    def __init__(self, name):
        self.name = name
        self.products = []
    def add_product(self, name, available):
        product = Product(name, available)
        self.products.append(product)
        return "Item added successfully."
    def search_product(self, name):
        for product in self.products:
         if product.name == name:
                return product.check_availability()
        return f"Sorry, the {self.name} is not found."
# Instantiate an object of ProductManager
product_manager = ProductManager("Fruit")
# Add some products to the product manager
product_manager.products.append(Product("Mango", True))
product_manager.products.append(Product("Pineapple", False))
product_manager.products.append(Product("Watermelon", True))
# Search for a product
print(product_manager.search_product("Mango"))
print(product_manager.search_product("Watermelon"))


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
        return "item added successfully"
    
    def search_product(self, name):
        for product in self.products:
            if product.name == name:
                return product.check_availability()
        return f"Sorry, the {name} is not found ."

