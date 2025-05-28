import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    chars = string.ascii_letters + string.digits + string.punctuation
    # Ensure at least one character from each category
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    password += random.choices(chars, k=length - 4)
    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        print("Generated password:", generate_password(length))
    except Exception as e:
        print("Error:", e)