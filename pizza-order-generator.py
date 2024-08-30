# This project helps you order a pizza!

# User input for their pizza order.
print("Welcome to Python Pizza Deliveries!")
size=input("What size pizza would you like? S M or L?: ")
pepperoni=input("Would you like pepperoni? Y or N: ")
extra_cheese=input("Would you like extra cheese? Y or N: ")
bill = 0


# Work out the size of the pizza
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Please input a proper pizza size.")

# Work out if they want pepperoni or not
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Work out if they want extra cheese or not
if extra_cheese == "Y":
    bill += 1

# Output the bill total
print(f"Your final bill is: ${bill}.")
