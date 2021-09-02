print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

z = print(str(name1 + name2))

a = z.lower()

b = 0

# Made use of += to add the values so I won't have to use multiple variables
b += a.count("t")

b += a.count("r")

b += a.count("u")

b += a.count("e")

b += a.count("l")

b += a.count("o")

b += a.count("v")

b += a.count("e")

print(b)







