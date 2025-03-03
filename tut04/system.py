import hashlib
import os
import json

# File to store user credentials
db_file = "users.json"

def load_users():
    """Load users from a JSON file."""
    if os.path.exists(db_file):
        with open(db_file, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    """Save users to a JSON file."""
    with open(db_file, "w") as f:
        json.dump(users, f)

def hash_password(password, salt):
    """Hash a password using SHA-256 with a salt."""
    return hashlib.sha256((salt + password).encode()).hexdigest()

def register(username, password):
    """Register a new user with a hashed password and salt."""
    users = load_users()
    if username in users:
        return "Username already exists."
    
    salt = os.urandom(16).hex()  
    password_hash = hash_password(password, salt)
    
    users[username] = {"salt": salt, "password_hash": password_hash}
    save_users(users)
    return "User registered successfully."

def login(username, password):
    """Authenticate a user by hashing input password and comparing it."""
    users = load_users()
    if username not in users:
        return "Invalid username or password."
    
    salt = users[username]["salt"]
    stored_hash = users[username]["password_hash"]
    
    if hash_password(password, salt) == stored_hash:
        return "Login successful."
    else:
        return "Invalid username or password."

if __name__ == "__main__":
    while True:
        action = input("Enter 'register' or 'login': ").strip().lower()
        if action not in ["register", "login"]:
            print("Invalid action. Try again.")
            continue
        
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        
        if action == "register":
            print(register(username, password))
        elif action == "login":
            print(login(username, password))
