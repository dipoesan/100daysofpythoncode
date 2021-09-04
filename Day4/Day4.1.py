import random

print("Welcome to the virtual coin toss program")

head_tails = random.randint(0, 1)

if head_tails == 1:
    print("Heads")
else:
    print("Tails")