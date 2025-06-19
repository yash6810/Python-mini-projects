import random 
import string

def simple_password(length=12):
    c = string.ascii_letters + string.digits + string.punctuation
    p = ''.join(random.choice(c) for i in range(length))
    return p

password_length = 10
my_password = simple_password(password_length)
print(f"Generated Password: {my_password}")
