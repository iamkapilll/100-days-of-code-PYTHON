import random
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
game_image = [rock, paper, scissors]
print("welcome to the ROCK, PAPER, SCISSORS GAME!!!!!!")
user_input = int(input("what do you wanna choose 0 = rock,1 = paper,2 = scissor\n"))
# 0, 1, 2
print(game_image[user_input])

computer_choice = random.randint(0,2)
print("computer choose")
print(game_image[computer_choice])

if user_input >= 3 or user_input < 0:
    print("YOU TYPED INVALID NUMBER")
elif user_input == 0 and computer_choice == 2:
    print("YOU WON!!")
elif computer_choice == 0 and user_input == 2:
    print("YOU LOOSE!!")
elif user_input > computer_choice:
    print("YOU WON")
elif computer_choice > user_input:
    print("YOU LOOSE!!")
elif user_input == computer_choice:
    print("ITS A DRAW!!")