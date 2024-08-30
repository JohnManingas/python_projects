print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#First Question
print("You make your way onto the island and come across a road.\n")
left_right=input("Which way would you like to go left or right?\n")
if left_right == "left":

    # Second Question
    print("You've made you way on one side of a river. You can swim across or wait for a boat to pick you up.")
    swim=input("Would you like to swim or wait?\n")
    if swim == "wait":

    # Third Question
        print("Crossing the river has brought you to the entrance of a crypt with stairs leading downwards.")
        print("Making your way down has brought you to an opening.")
        door=input("You arrive in front of 3 doors, each of which are colored differently. Which color door will you choose: blue, red or yellow?\n")

        # Fourth Question
        if door == "yellow":
            print("Congratulations! You Win!")
        elif door == "blue":
            print("You have been eaten by beasts. Game Over.")
        elif door == "red":
            print("You have been burned by fire. Game Over")
        else:
            print("Game Over.")

    #Second Question Closing Else Statement
    else:
        print("Attacked by trout. Game Over")
#First Question Closing Else Statement
else:
    print("Fall into a hole.\n Game Over.")
