class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserManager:
    def __init__(self):
        self.users = []
        self.logged_in_user = None
    
    def add_user(self, username, password):
        user = User(username, password)
        self.users.append(user)
    
    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.logged_in_user = user
                return True
        return False
    
    def is_logged_in(self):
        return self.logged_in_user is not None
    
    def logout(self):
        self.logged_in_user = None

# Example usage:
user_manager = UserManager()

# Sign up a new user
user_manager.add_user('val_buraje', 'password123')

# Log in the user
success = user_manager.login('val_buraje', 'password123')
if success:
    print('Login successful!')
else:
    print('Incorrect username or password.')

# Check if the user is logged in
if user_manager.is_logged_in():
    print(f'Logged in as {user_manager.logged_in_user.username}.')
else:
    print('Not logged in.')

# Log out the user
user_manager.logout()
print('Logged out.')