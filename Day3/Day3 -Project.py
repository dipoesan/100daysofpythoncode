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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

left_right = input("You are at a cross road. Are you going left or right? l or r\n")

if left_right == "l":
    swim_wait = input("You have come to a lake, and there is an island across. Do you want to swim to the island or wait for a boat? swim or wait\n")
    if swim_wait == "wait":
        door = input("You arrive at the island unharmed and are presented with 3 doors. Which door are you opening? red, blue, yellow\n")
        if door == "red":
            print("You were burnt by fire, Game Over!!!!!")
        elif door == "blue":
            print("You were eaten by beasts, Game Over!!!!!")
        elif door == "yellow":
            print("You Won!!!!!")
        else:
            print("Game Over!!!!!")
    else:
        print("You were attacked by a trout, Game Over!!!!!")
else:
    print("You fell in a hole, Game Over!!!!!")