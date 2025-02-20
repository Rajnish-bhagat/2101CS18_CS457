import re

def validate_password(password, criteria):
    if len(password) < 8:
        return False, "Less than 8 Characters"
    
    allowed_special_chars = set("!@#")
    errors = []
    
    if '1' in criteria and not any(c.isupper() for c in password):
        errors.append("Missing Uppercase letters")
    if '2' in criteria and not any(c.islower() for c in password):
        errors.append("Missing Lowercase letters")
    if '3' in criteria and not any(c.isdigit() for c in password):
        errors.append("Missing Numbers")
    if '4' in criteria:
        special_chars = set(re.findall(r'[^a-zA-Z0-9]', password))
        if not special_chars:
            errors.append("Missing Special characters")
        elif not special_chars.issubset(allowed_special_chars):
            errors.append(f"Contains invalid special characters: {''.join(special_chars - allowed_special_chars)}")
    
    return (False, ", ".join(errors)) if errors else (True, "Valid")

# Get user input for criteria
criteria_input = input("Enter the criteria you want to check (1 for Uppercase, 2 for Lowercase, 3 for Numbers, 4 for Special Characters): ")
criteria = set(criteria_input.split(","))

# Read passwords from file
valid_count = 0
invalid_count = 0

with open("input.txt", "r") as file:
    passwords = file.readlines()

for password in passwords:
    password = password.strip()
    is_valid, message = validate_password(password, criteria)
    if is_valid:
        valid_count += 1
    else:
        invalid_count += 1
    print(f"'{password}' is {message}.")

print(f"Total Valid Passwords: {valid_count}")
print(f"Total Invalid Passwords: {invalid_count}")
