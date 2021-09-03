print("Welcome to the Love Calculator!")

# Made use of the .lower() method to transform user input to lowercase
name1 = (input("What is your name? \n")).lower()
name2 = (input("What is their name? \n")).lower()

# Concatenated both variables 
z = name1 + name2

# Printed z to see what the output of the above concatenation would look like
# print(z)

a = 0
b = 0

# Made use of += to add the values so I won't have to use multiple variables
a += z.count("t")

a += z.count("r")

a += z.count("u")

a += z.count("e")

b += z.count("l")

b += z.count("o")

b += z.count("v")

b += z.count("e")

# Converted the results of combining both variables to an integer
y = int(f"{a}{b}")

# Wanted to check what the above would give me
#Also wanted to check if it gave me the right data type
# print (y)
# print(type(y))

if y < 10 or y > 90:
    print (f"Your score is {y}, you go together like coke and mentos.")

elif y == 40 and y <= 50:
    print(f"Your score is {y}, you are alright together.")

else:
    print(f"Your score is {y}.")