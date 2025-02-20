import random
import string

def generate_passwords(count=1000):
    special_chars = "!@#"
    for _ in range(count):
        length = random.randint(6, 16)
        password = "".join(random.choices(string.ascii_letters + string.digits + special_chars, k=length))
        yield password

def save_passwords(filename="input.txt", count=1000):
    with open(filename, "w") as file:
        for password in generate_passwords(count):
            file.write(password + "\n")

if __name__ == "__main__":
    save_passwords()
    print("Passwords saved to input.txt")
