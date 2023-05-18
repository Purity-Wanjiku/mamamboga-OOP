class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
         self.email = email

class UserManager:
    def __init__(self):
        self.users = []
    
    def add_user(self, username, password,email):
        user = User(username, password,email)
        self.users.append(user)
    
    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

# Example usage:
user_manager = UserManager()

# Sign up a new user
user_manager.add_user('val_buraje', 'password123')

# Verify the user's login credentials
user = user_manager.get_user_by_username('john_doe')
if user and user.password == 'password123':
    print('Login successful!')
else:
    print('Incorrect username or password.')
