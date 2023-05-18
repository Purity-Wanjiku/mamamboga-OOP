
   
class signup:
    def __init__(self,First_Name,Last_Name,Email_Address,Phone_No,Account_password,Password_Confirm) :
        self.First_Name=First_Name
        self.Last_Name=Last_Name
        self.Email_Address=Email_Address
        self.Phone_No=Phone_No
        self.Account_password=Account_password   
        self.Password_Confirm=Password_Confirm
       
        
# password confirmation checks if the account password is correct

    def validate_password(self):
        if(self.Account_password==self.Password_Confirm):
            print( f"Valid password")
        else:
            print(f"Please enter the correct password")

    def log_in (self,email,password):
        if email== self.Email_Address:
            return (f"Email successful")   
        elif password== self.Account_password:
            return(f"Password successful")
        else :
            return(f"Your email does not match your password")
