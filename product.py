class Product:
    def __init__(self, name):
        self.name = name
        self.products = []
        
    def add_product(self, name):
        self.products.append(name)
        return f"{name} has been added to {self.name}."
    
    def search_product(self, name):
        for product in self.products:
            if product == name:
                return f"{product} is available"
        return f"{product} is not available"
    
    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            return f"{product} has been removed from products"
        else:
            return f"{product} is not in products."
        
my_object = Product("")

# Add some products to the Product 
my_object.add_product("Orange")
my_object.add_product("Pineapple")
my_object.add_product("Watermelon")

# Search for a product
print(my_object.search_product("Mango"))
print(my_object.search_product("Pineapple"))
print(my_object.search_product("Watermelon"))

# Remove a product
print(my_object.remove_product("Orange"))
print(my_object.remove_product("Pears"))

# Check if the product has been removed
print(my_object.products)


