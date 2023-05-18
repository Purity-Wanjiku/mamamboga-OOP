class Notify:
    def __init__(self,name,order_made):
        self.name = name
        self.order_made = order_made
        self.is_read = False

     
    def mark_as_read(self):
       self.is_read = True
   
    def send_notification(self):
        item_order={
            "name":self.name,
            "orders":self.order_made
        }
        return item_order
    
    # method checks if there are new orders and if the notifications have been seen
    
    def check_notifications(self):
        if self.order_made > 0 and not self.is_read:
            print("Hello, you have {}  new orders from {}.".format(self.number_of_orders,self.name))
        elif self.is_read:
            print("You have no new notification")
name = "Hellen"
order_made = 5

# instantiate a new variable and call the class
new_message = Notification(name,order_made)
notification_dict = new_message.send_notification()
print(notification_dict)
new_message.check_notifications()
new_message.mark_as_read()
