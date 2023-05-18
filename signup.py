class User:
    def __init__(self, username, email, password):
        self.username = username
         self.email = email
        self.password = password

class UserManager:
    def __init__(self):
        self.users = []
    
    def add_user(self, username, email, password):
        user = User( username, email, password)
        self.users.append(user)
    
    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

# Example usage:
user_manager = UserManager()

# Sign up a new user
user_manager.add_user('val_buraje', 'val@gmail.com', 'password123')

# Verify the user's login credentials
user = user_manager.get_user_by_username('val_buraje')
if user and user.password == 'password123':
    print('Login successful!')
else:
    print('Incorrect username or password.')
