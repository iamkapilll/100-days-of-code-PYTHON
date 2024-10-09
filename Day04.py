import random
# random modules:::

random_integer = random.randint(0,1)
print(random_integer)


random_float = random.uniform(1.0,5.0)
print(random_float)


random_number = random.random()
print(random_number)


head_or_tail = random.randint(0,1)
if head_or_tail == 0:
    print(f"{head_or_tail} is head")
else:
    print(f"{head_or_tail} is tails")


fruits = ['apple', 'banana','cherry']
random_choice = random.choice(fruits)
print(random_choice)


numbers = [1,2,3,4,5,6,7,8]
random.shuffle(numbers)
print(numbers)

# lists:::

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

states_of_america[1] = "Pencilvania"

states_of_america.append("kapil's land")

states_of_america.extend(["kapil's land", "puri's Land"])

print(states_of_america)

friends = ["kapil", "suyog", "kshitiz", "puri", "abishek"]
print(friends)
# option 1,,
print(random.choice(friends))

# option 2,,
print("WAITER :  sir bill please..\n "
      "Friends : choose from the boat..")
friends_bill = random.randint(1,4)
print(friends_bill)

print(friends[friends_bill])

# ..THE TWO LISTS INSIDE ANOTHER LIST...

dirty_Dozen = ["stroberries", "Spinach", "kale","nectarines", "apples"
               "grapes"," peaches"]
fruits = ["apple", "orange", "banana", "pineappple"]
vegetables = ["potato","tomato", "garlic", "ginger"]

dirty_Dozen = [fruits,vegetables]

print(dirty_Dozen)