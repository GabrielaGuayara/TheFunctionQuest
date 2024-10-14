# The Mighty Calculator Functions
def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero!"

# Fibonacci Function
def fibonacci(n):
    if n <= 0:
        return "Invalid number"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Decoder Function
def decode_message(encoded_message, cipher_dict):
    decoded_message = ''.join(cipher_dict.get(char, char) for char in encoded_message)
    return decoded_message

# Email Validator Function
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# The Mighty Calculator Functions
print("Calculator Operations:")
print("The sum is:", add_numbers(5, 3))
print("The difference is:", subtract_numbers(10, 4))
print("The product is:", multiply_numbers(6, 2))
print("The quotient is:", divide_numbers(15, 0))

# The Fibonacci Function
try:
    user_input = int(input("\nEnter a positive integer for Fibonacci: "))
    print(f"The Fibonacci number at position {user_input} is: {fibonacci(user_input)}")
except ValueError:
    print("Please enter a valid integer.")

# The Decoder Function
cipher = {
    'a': 'm', 'b': 'n', 'c': 'o', 'd': 'p', 'e': 'q',
    'f': 'r', 'g': 's', 'h': 't', 'i': 'u', 'j': 'v',
    'k': 'w', 'l': 'x', 'm': 'y', 'n': 'z', 'o': 'a',
    'p': 'b', 'q': 'c', 'r': 'd', 's': 'e', 't': 'f',
    'u': 'g', 'v': 'h', 'w': 'i', 'x': 'j', 'y': 'k', 'z': 'l'
}

encoded_message = input("\nEnter the encoded message: ")
print("Decoded message:", decode_message(encoded_message, cipher))

# Calling the Email Validator Function
email_input = input("\nEnter an email address to validate: ")
if is_valid_email(email_input):
    print("The email address is valid.")
else:
    print("The email address is invalid.")
