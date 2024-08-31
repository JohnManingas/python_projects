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

#Place rock paper scissors into a list
game_list=[rock,paper,scissors]

# Import random to utilize rand functions
import random

# Acquire user input
# Transform into integer for if-else conditions
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
print(game_list[user_choice])

# Acquire random computer input
# Output image of computer choice
computer_choice=random.randint(0,2)
print("Computer chose:")
print(game_list[computer_choice])

# Use if-else statements to establish win condition logic
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("you lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")

