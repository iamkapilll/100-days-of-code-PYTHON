# function 
def my_function():
    print("hello")
    print("bye")
my_function()

# multiplication_table using function and loop
def multiplication_table(number):
    for i in range(1,11):
        print(f"{number} * {i} = {number * i}")

num = int(input("Enter a number:"))
multiplication_table(num)


# for loop 
for item in range(0,10):
    print(item)


# while loop 
i = 1
while i < 6:
    print(i)
    i+=1