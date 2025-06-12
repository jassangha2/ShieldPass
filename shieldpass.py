import getpass
import re

def is_strong_password(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    if length_error or digit_error or uppercase_error or lowercase_error or symbol_error:
        return False
    return True

def main():
    print("🛡️ Welcome to ShieldPass!")
    password = getpass.getpass("Enter your password: ")

    if is_strong_password(password):
        print("✅ Your password is strong.")
    else:
        print("❌ Your password is weak. Try adding uppercase, lowercase, symbols, and numbers.")

if __name__ == "__main__":
    main()
    