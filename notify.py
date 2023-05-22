class Notify:
    def __init__(self, name, order_made):
        self.name = name
        self.order_made = order_made
        self.is_read = False

    def mark_as_read(self):
        self.is_read = True

    def send_notification(self):
        item_order = {
            "name": self.name,
            "orders": self.order_made
        }
        return item_order

    def check_notifications(self):
        if self.order_made > 0 and not self.is_read:
            print("Hello, you have {} new orders from {}.".format(self.order_made, self.name))
        elif self.is_read:
            print("You have no new notifications.")
            


# Example usage:
name = input("Enter your name: ")
order_made = int(input("Enter the number of orders made: "))

new_notification = Notify(name, order_made)

new_notification.check_notifications()
new_message.check_notifications()
new_message.mark_as_read()
