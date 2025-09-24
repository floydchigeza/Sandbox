min_length= 10

password = input("Enter a password: ")
while len(password) != min_length:
    print(f"Password must be at least {min_length} characters long.")
    password = input("Enter a password: ")

print('*' * len(password))