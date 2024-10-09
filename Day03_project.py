# TREASER GAME 
print("welcome to the treser finding game")
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
decision_1 = input("Where do you want to go? left or right\n")
if decision_1 == "left":
    print("Congrats! You made it one step closer to the treasure.")
    decision_2 = input("Do you want to swim or wait?\n")
    if decision_2 == "wait":
        print("The boat arrived, and you made it to the next step.")

        decision_3 = input("Which door do you want to open? red, blue, or yellow\n")
        if decision_3 == "red":
            print("You died due to FIRE!! GAME OVER!")
        elif decision_3 == "blue":
            print("You died due to BEASTS!! GAME OVER!")
        elif decision_3 == "yellow":
            print("Congrats! You FOUND THE TREASURE!")
        else:
            print("Please enter a correct color decision.")
    elif decision_2 == "swim":
        print("You died due to a shark. GAME OVER!")
    else:
        print("Please enter a valid choice: 'swim' or 'wait'.")
elif decision_1 == "right":
    print("GAME OVER!")
else:
    print("Please enter a valid choice: 'left' or 'right'.")