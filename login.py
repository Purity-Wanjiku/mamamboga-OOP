class Login:
    def __init__(self,email_address,password):
        self.email_address=email_address
        self.password=password
    def update_email_address(self, new_email_address):
        self.email_address = new_email_address
    def input_password(self, new_password):
        self.password = new_password
    def __str__(self):
        return f"{self.email_address},{self.password}"