#Let's order some pizza

#Greet our guests!
print("Welcome to Marky's pizza!")

#Retrieve input from our customers
#automatically translates user input into lowercase
size=input("What size pizza would you like? 'S' for Small, 'M' for Medium, 'L' for Large'\n").lower()
pepperoni=input("Would you like pepperoni? 'Y' for yes, 'N' for no\n").lower()
cheese=input("Would you like extra cheese? 'Y' for yes, 'N' for no\n").lower()

#Initiate a variable for the bill
bill = 0

#Calculate the amount for the size of the pizza
if size == 's':
    bill += 15
elif size == 'm':
    bill += 20
elif size == 'l':
    bill += 25
else:
    print("Please choose a proper size for the pizza")

# Include the price of cheese
# Price of cheese depends on size of pizza
if cheese == 'y':
    if size == 's':
        bill += 1
    elif size == 'm' or size == 'l':
        bill += 2

#Find if they want pepperoni
#Pepperoni depends on the size of the pizza
if pepperoni == 'y':
    if size == 's':
        bill += 2
    elif size == 'm' or size == 'l':
        bill += 3

# Calculate the total amount for the bill
print(f"Your final bill is ${bill}.")
