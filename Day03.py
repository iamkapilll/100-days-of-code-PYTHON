# conditional statement

#rollercoaster example: if else statement
print("welcome to the rollercoaster")
height = int(input("what is your height in cm?\n"))
if height >= 120:
  print("you can ride the rollercoaster")
else:
  print("sorry, you have to grow taller before you can ride")

# modulo
# print(10%3)

# odd and even number

number = int(input("Enter an integer:"))
if number %2 == 0:
  print(f"The {number} is an even number")
else:
  print(f"The {number} is an odd number")

# Nested if else

print("welcome to the rollercoaster")
height = int(input("what is your height in cm?\n"))
bill = 0
if height >= 120:
  print("you can ride the rolercoaster")
  age = int(input("what is your age?\n"))
  if age <12:
    bill = 5
    print("child tickets pay $5")
  elif age <= 18:
    bill = 7
    print("adults ticket pay $7")
  elif age >18 and age <45:
    bill = 12
    print("youth ticket pay $12")
  elif age >= 45 and age <= 55:
    bill = 0
    print("The midlife crisis ticket is free")
  else:
    print("please enter a valid age")
  photo = input("want photos (Y/N)?")
  if photo == "y":
    bill += 3
    
  print(f"The total bill is ${bill}")

else:
  print("sorry, you have to grow taller before you can ride")

# pizza delliviry

print("welcome to the pizza delivery")
bill = 0
size = input("what size pizza do you want? S, M, L\n")
pepperoni = input("do you want pepperoni? Y orN\n")
cheese = input("do you want extra cheese? Y or N\n")
if size == "s":
  bill += 15
elif size == "m":
  bill += 20
elif size == "l":
  bill += 25
else:
  print("plese enter the correct size")

if pepperoni == "y":
  if size == "s":
    bill += 2
  else:
    bill += 3

if cheese == "y":
  bill += 1

print(f"your final bill is ${bill}")