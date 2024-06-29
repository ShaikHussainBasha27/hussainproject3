"""To Generate strong and secure passwords with Python for your accounts."""
import secrets
import string

def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    secure_password = ''.join(secrets.choice(alphabet) for i in range(length))
    return secure_password

def password_generator():
    num_passwords = int(input("How many passwords do you want to generate? "))
    
    while True:
        if num_passwords <= 0:
            print("Please enter a valid number greater than zero.")
            num_passwords = int(input("How many passwords do you want to generate? "))
        else:
            break
    
    passwords = []
    for i in range(num_passwords):
        while True:
            length = input(f"Enter the length of Password #{i + 1}: ")
            if length.isdigit() and int(length) >= 3:
                length = int(length)
                break
            else:
                print("Minimum length of password should be 3. Please enter a valid length.")
        
        passwords.append(generate_password(length))
    
    print("\nGenerating Passwords:")
    for idx, password in enumerate(passwords, start=1):
        print(f"Password #{idx}: {password}")

# Call the function to start the password generation process
password_generator()