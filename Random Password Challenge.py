import random
import string
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
password_chars = (
    random.choice(lowercase) +
    random.choice(uppercase) +
    random.choice(numbers)
)
for i in range(5):
    password_chars += random.choice(lowercase + uppercase + numbers)
password_list = list(password_chars)
random.shuffle(password_list)
password = ''.join(password_list)
print("Generated Password:", password)