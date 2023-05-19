class ItemsAvailable:
    def __init__(self,item_name,price,addtocart, available_groceries) :
        self.item_name=item_name
        self.price=price
        self.addtocart={}
        self.groceries = {}
        
    def add_item(self,add):
        self.add=self.addtocart

#Checking if the item selection is available in stock

        if self.item_name in self.groceries and self.price in self.groceries:
            self.add==True
            print(f"{self.item_name} added to basket")
            
        else:
            self.add == False
            print(f"{self.item_name} is not available")

# returning the final state of the button "add to cart"

        return self.add

# use example


item = ItemsAvailable("pineapple", 200, False, {"pineapple": 180, "mango": 100})

print(item.add_item(False))


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

