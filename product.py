class Product:
    def __init__(self, name):
        self.name = name
        self.products = []
        
    def add_product(self, name):
        product = Product(name)
        self.products.append(product)
        return "Item added successfully."
    
    def search_product(self, name):
        for product in self.products:
         if product == name:
            return product
        return None
    
my_object =  Product("")
# Add some products to the Product 
my_object.products.append("Orange")
my_object.products.append("Pineapple")
my_object.products.append("Watermelon")
# Search for a product
print(my_object.search_product("Mango"))
print(my_object.search_product("Pineapple"))
print(my_object.search_product("Watermelon"))
print(my_object.products)

