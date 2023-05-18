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

class ProductCatalog:
    def __init__(self):
        self.products = []
    
    def add_product(self, name, product_type, availability, price, description):
        product = Product(name, product_type, availability, price, description)
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


product_catalog.add_product('apple', 'fruit', 10, 1.0, 'A juicy fruit with a crisp texture.')

product = product_catalog.get_product_by_name('apple')
if product:
    product.update_availability(5)
    product.update_price(1.5)
    product.update_description('A popular fruit with many health benefits.')
    print('Product updated.')
else:
    print('Product not found.')


product_catalog.remove_product('apple')
print('Product removed.')