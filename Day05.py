# LOOPS:::

fruits = ['apple','peach','pear']
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")



# for x in 'apple':
#     print(x)



scores = [50,4,50,3,204,0,60]
total_sum = sum(scores)
print(total_sum)

sum = 0
for score in scores:  #for total sum
    sum += score
print(sum)

max = 0
for score in scores:   # for maximum number
    if max < score:
        max = score
print(max)




for number in range(1,11,3):
    print(number)


sum = 0
for num in range(1,101):  # sum of numbers from 1 to 100:
    sum += num
print(sum)


# [Q.]...You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"



for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)