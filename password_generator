import random
import string


def password_gen(password_length):
    try:
        password_length = int(password_length)
        if 28 >= password_length >= 8:
            return "".join(random.choices(string.ascii_letters + string.digits, k=password_length))
        else:
            print("Password length should be at a range of 8 to 28")
            
    except ValueError:
        print("Please input a Integer")


user_password_length = input("Your desired password length (8 to 28): ")
print(password_gen(user_password_length))


