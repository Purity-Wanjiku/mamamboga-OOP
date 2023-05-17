class Sign_up:
    def __init__(self,full_name,email_address,password,password_confirmation):
        self.full_name=full_name
        self.email_address=email_address
        self.password=password
        self.password_confirmation=password_confirmation
    def update_full_name(self, new_full_name):
        self.full_name = new_full_name
    def update_email(self, new_email_address):
        self.email_address = new_email_address
    def update_password(self, new_password):
        self.password = new_password
    def update_password_confirmation(self, new_password_confirmation):
        self.password_confirmation = new_password_confirmation
    def __str__(self):
       return f"{self.full_name},{self.email_address},{self.password},{self.password_confirmation} "