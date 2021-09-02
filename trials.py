print ("Welcome to Pizaa Go")

small = 15
medium = 20
large = 25

per = 3
cheese = 1

size = input("what size you want! small medium large! ")

perpi = input("do you you want perpi! Y or N ")

extra_cheese = input("do you you want extra cheese! Y or N ")

if size == "small" and perpi == "Y" and extra_cheese == "Y": print (f"Sir pay {small + per + cheese}")

elif size == "medium"and perpi == "Y" and extra_cheese == "Y": print (f"Sir pay {medium + per + cheese}")

elif size == "large" and perpi == "Y" and extra_cheese == "Y": print (f" Sir pay {large + per + cheese}")

if size == "small" and perpi == "Y" and extra_cheese == "N": print (f"Sir pay {small + per }")

if size == "small" and perpi == "N" and extra_cheese == "Y": print (f"Sir pay {small + cheese }")

if size == "medium" and perpi == "Y" and extra_cheese == "N": print (f"Sir pay {medium + per }")

if size == "medium" and perpi == "N" and extra_cheese == "Y": print (f"Sir pay {medium + cheese }")

if size == "large" and perpi == "Y" and extra_cheese == "N": print (f"Sir pay {large + per }")

if size == "large" and perpi == "N" and extra_cheese == "Y": print (f"Sir pay {large + cheese }")

print ("Bon appetit ")