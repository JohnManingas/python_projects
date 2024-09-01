# Password Generator Project
# Introduce lists for password utilization
from symbol import pass_stmt

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Introduce random tools
import random

# Print welcome statement
# Introduce user input
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# EASY LEVEL
# Create a starting value for password which will be added to by end of function
# password = ""
#
# # Pull user input for amount of letters in for loop
# for char in range(0, nr_letters):
#     password += random.choice(letters)
#
# # Pull user input for amount of numbers
# for num in range(0, nr_numbers):
#     password += random.choice(numbers)
#
# # Pull user input for amount of symbols
# for sym in range (0, nr_symbols):
#     password += random.choice(symbols)
#
# print(f"Your new password is: {password}")


# HARD LEVEL

#Create a starting value to input password into a list
password_list=[]

# Add a random character from each list to add into password list
for char in range(0,nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

print(password_list)

# shuffle the password
random.shuffle(password_list)
print(password_list)

# Enter the password into a for loop to transfer it into string type
password = ""
for char in password_list:
    password += char

# End the program
print(f"Your new password is: {password}")
