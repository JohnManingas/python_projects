# Rock, Paper, Scissors game
# Define output for rock, paper and scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Import random to utilize rand functions
import random

# Acquire user input
# Transform into integer for if-else conditions
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

# Acquire random computer input
computer_input=random.randint(0,2)

# Print output for user input
# Within each user input, include if statements for computer input conditions
if user_choice == 0:
    print(rock)
    if computer_input == 0:
        print(f"Computer chose: {rock}")
        print("It's a draw")
    elif computer_input == 1:
        print(f"Computer chose: {paper}")
        print("You lose")
    else:
        print(f"Computer chose: {scissors}")
        print("You won!")
elif user_choice == 1:
    print(paper)
    if computer_input == 0:
        print(f"Computer chose: {rock}")
        print("You won!")
    elif computer_input == 1:
        print(f"Computer chose: {paper}")
        print("It's a draw")
    else:
        print(f"Computer chose: {scissors}")
        print("You lose")
elif user_choice == 2:
    print(scissors)
    if computer_input == 0:
        print(f"Computer chose: {rock}")
        print("You lose")
    elif computer_input == 1:
        print(f"Computer chose: {paper}")
        print("You won!")
    else:
        print(f"Computer chose: {scissors}")
        print("It's a draw")
else:
    print("Please choose 0,1, or 2")
