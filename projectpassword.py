import string

print("Password Strength Checker")
print("--------------------------")

# take password from user
password = input("Enter your password: ")

strength = 0

# check length
if len(password) >= 8:
    strength += 1

# check uppercase
for char in password:
    if char.isupper():
        strength += 1
        break

# check lowercase
for char in password:
    if char.islower():
        strength += 1
        break

# check digit
for char in password:
    if char.isdigit():
        strength += 1
        break

# check special character
special_characters = string.punctuation
for char in password:
    if char in special_characters:
        strength += 1
        break

# final result
print("\nPassword Strength Result:")

if strength <= 2:
    print("Weak Password")
elif strength == 3 or strength == 4:
    print("Medium Password")
else:
    print("Strong Password")
