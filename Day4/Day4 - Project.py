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


options = [rock, paper, scissors]

computers_option = random.randint(0, 2)

# print (y)

choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors."))

if choice == 0:
    print(options[0])
    if computers_option == 0:
        print("Computer chose:\n " + options[0])
        print("It is a draw")
    if computers_option == 1:
        print("Computer chose:\n " + options[1])
        print("You lose")
    if computers_option == 2:
        print("Computer chose:\n " + options[2])
        print("You won")
if choice == 1:
    print(options[1])
    if computers_option == 0:
        print("Computer chose:\n " + options[0])
        print("You won")
    if computers_option == 1:
        print("Computer chose:\n " + options[1])
        print("It is a draw")
    if computers_option == 2:
        print("Computer chose:\n " + options[2])
        print("You lose")
if choice == 2:
    print(options[2])
    if computers_option == 0:
        print("Computer chose:\n " + options[0])
        print("You lose")
    if computers_option == 1:
        print("Computer chose:\n " + options[1])
        print("You won")
    if computers_option == 2:
        print("Computer chose:\n " + options[2])
        print("It is a draw")
else:
    print("You did not make the right selection. Please start again.")
