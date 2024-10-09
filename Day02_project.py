# (Q).. calculate the BMI of a person
height = 1.65
weight = 84
squared_height = height**2
bmi = weight/squared_height
print(bmi) # gives the result in float outputs 30.853998347...
print(int(bmi)) # outputs = 30 will release all the decimal palces but not round
print(round(bmi)) # results in roundoff the 30.853998347...in 31

#(Q).. calculate the tip calculator
print("Welcome to the tip calculator!")

# Get the total bill amount
total = float(input("What was the total bill? $"))

# Get the tip percentage
tip = float(input("How much tip would you like to give? 10, 20, 30? "))

# Calculate the total amount including the tip
tip_calc = total * (tip / 100) + total
print(f"The final total (total + tip) is ${tip_calc:.2f}")

# Get the number of people to split the bill
bill_split = int(input("How many people to split the bill? "))

# Calculate the amount each person should pay
final_bill = tip_calc / bill_split

print(f"Each person should pay ${final_bill:.2f}")

