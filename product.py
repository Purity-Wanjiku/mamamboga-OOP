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


item = ItemsAvailable("kiwi", 200, False, {"kiwi": 200, "mango": 100})

print(item.add_item(False))
