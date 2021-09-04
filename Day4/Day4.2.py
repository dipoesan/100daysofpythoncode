import random

names_string = input("Give me everybody's names, separated by a comma. \n")

names = names_string.split(", ")

a = len(names) - 1

y = random.randint(0, a)

print((names[y]) + " is going to pay for our meal today!!!")