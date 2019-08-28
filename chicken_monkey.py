# Write a program that prints the numbers from 1 to 100. You can use Python's range() to quickly make a list of numbers.

# For multiples of five (5, 10, 15, etc.) print "Chicken" instead of the number
# For the multiples of seven (7, 14, 21, etc.) print "Monkey".
# For numbers which are multiples of both five and seven print "ChickenMonkey".
# To determine if a number can be evenly divided by 5 or 7, use the Python modulo operator.

# range(start, stop, step)


    # my_range = range(1, 101)
    # for number in my_range:
    # print(number)

def my_numbers():
    my_range = range(1, 101)
    for num in my_range:
        if num % 5 == 0 & num % 7 == 0:
            print ("ChickenMonkey")
        elif num % 5 == 0:
            print("Chicken")
        elif num % 7 == 0:
            print("Monkey")
        else:
            print(num)

my_numbers()



#another way:

# for i in range(100):
#     if (i % 5) == 0 and (i % 7) == 0:
#         print("ChickenMonkey")
#     elif (i % 5) == 0:
#         print("Chicken")
#     elif (i % 7) == 0:
#         print("Monkey")
#     else:
#         print(i)





