
   
class Signup:
    def __init__(self,first_Name,last_name,email_address,phone_no,account_password,password_confirm) :
        self.first_name=first_name
        self.last_name=last_name
        self.email_address=email_address
        self.phone_no=phone_no
        self.account_password=account_password   
        self.password_confirm=password_confirm
       
      
       #logging in after creating an account

    def validate_password(self):
        if(self.account_password==self.password_confirm):
            print( f"Valid password")
        else:
            print(f"Please enter the correct password")

    def log_in (self,email,password):
        if email== self.email_address:
            return (f"Email successful")   
        elif password== self.account_password:
            return(f"Password successful")
        else :
            return(f"Your email does not match your password")
