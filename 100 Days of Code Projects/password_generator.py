import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!\n")

num_lett = int(input("How many letters would you like your password to be?\n "))
num_symb = int(input("How many symbols would you like to add to your password?\n"))
num_amount = int(input("How many numbers would you like to add to your password?\n"))

password_shuffle = []

for l in range(num_lett + 1):
    l = random.choice(letters)
    password_shuffle += l


for n in range(1, num_symb + 1):
    n = random.choice(numbers)
    password_shuffle += n


for s in range(1, num_amount + 1):
    s = random.choice(symbols)
    password_shuffle += s

random.shuffle(password_shuffle)

random_password = ""
for p in password_shuffle:
    random_password += p

print(f"Your generated password is: {random_password}")