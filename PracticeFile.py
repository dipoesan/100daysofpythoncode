# num_char = len (input("What is your name?\n"))

# new_num_char = str(num_char)

# print("Your name has " + new_num_char + " characters")

# 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆

# ####################################
# #Write your code below this line 👇

# print (type(two_digit_number))

# print (int(two_digit_number [0]) + int(two_digit_number [1]))

# 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# print (type(height))

# print (type(weight))

# height_squared = (float(height)) ** 2

# BMI = float(weight) / height_squared

# print (int (BMI))

# 🚨 Don't change the code below 👇
# age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# ninety_days = 90

# days = (ninety_days - int(age)) * 365 

# weeks = (ninety_days - int(age)) * 52

# months = (ninety_days - int(age)) * 12

# print (f"You have {days} days, {weeks} weeks, and {months} months left.")

print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))

if height>=120:
    print("You can ride on the rollercoaster")
    age = int(input("What is your age? "))
    bill = 0
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")
    take_photo = input("Do you want to take pictures? Y or N")
    if take_photo == "y":
        bill += 3
    print(f"Your total bill is ${bill}")
else:
    print("You cannot ride on the rollercoaster")
