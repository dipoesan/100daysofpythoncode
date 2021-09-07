print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))

tip = int(input("How much would you like to tip? 10, 12, or 15?"))

num_people = int(input("How many people are splitting the bill?"))

tip_percent = tip /100

tip_value = bill * tip_percent

bill_plus_tip = bill + tip_value

payment = bill_plus_tip / num_people

print(f"Each person should pay: ${round(payment, 2)}")