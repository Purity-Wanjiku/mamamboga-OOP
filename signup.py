
   class Signup:
    def __init__(self, first_name, last_name, email_address, phone_no, account_password, password_confirm):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone_no = phone_no
        self.account_password = account_password   
        self.password_confirm = password_confirm
       
    def validate_password(self):
        if self.account_password == self.password_confirm:
            print("Valid password")
        else:
            print("Please enter the correct password")

    def log_in(self, email, password):
        if email == self.email_address and password == self.account_password:
            return "Login successful"
        else:
            return "Invalid credentials. Please check your email and password and try again"

# Example usage:
signup_instance = Signup("Val", "Aketch", "valaketch@example.com", "1234567890", "password123", "password123")
signup_instance.validate_password()  # Output: Valid password
login_result = signup_instance.log_in("valaketch@example.com", "password123")
print(login_result)  # Output: Login successful
login_result = signup_instance.log_in("valaketch@example.com", "wrongpassword")
print(login_result)  # Output: Invalid credentials. Please check your email and password and try again

