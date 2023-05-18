class Product:
    def __init__(self, name, category, minimum-quantity, price):
        self.name = name
        self.category = category
        self.minimum-quantity = minimum-quantity
        self.price = price
    
    def update_name(self, name):
        self.name = name
    
    def update_category(self, category):
        self.category = category
    
    def update_minimum-quantity(self, minimum-quantity):
        self.minimum-quantity = minimum-quantity
        
    def update_price(self, price):
        self.price = price

class ProductCatalog:
    def __init__(self):
        self.products = []
    
    def add_product(self, name, category, price, minimum-quantity):
        product = Product(name, category, price, minimum-quantity))
        self.products.append(product)
    
    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
    
    def get_product_by_name(self, name):
        for product in self.products:
            if product.name == name:
                return product
            return None


product_catalog = ProductCatalog()


product_catalog.add_product('apple', 'fruit', 35, 250)

product = product_catalog.get_product_by_name('apple')
if product:
    product.update_category('Fruit')
    product.update_price(35)
    product.update_minimum-quantity(250)
    print('Product updated.')
else:
    print('Product not found.')


product_catalog.remove_product('apple')
print('Product removed.')
