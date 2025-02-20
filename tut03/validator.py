import re

def validate_password(password, criteria):
    if len(password) < 8:
        print(f"'{password}' is Invalid. Less than 8 Characters.")
        return
    
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
    
    if errors:
        print(f"'{password}' is Invalid. {', '.join(errors)}")
    else:
        print(f"'{password}' is Valid.")

# Get user input for criteria
criteria_input = input("Enter the criteria you want to check (1 for Uppercase, 2 for Lowercase, 3 for Numbers, 4 for Special Characters): ")
criteria = set(criteria_input.split(","))

# Password list
test_passwords = [
    "abc12345",
    "abc",
    "123456789",
    "abcdefg$",
    "abcdefgABHD!@313",
    "abcdefgABHD$$!@313",
]

# Validate passwords
for password in test_passwords:
    validate_password(password, criteria)
