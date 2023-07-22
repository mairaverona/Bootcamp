# import math function

import math
import statistics

# ask user to input 10 floats (integers or decimals) / store numbers on a list
# start empty list and then append numbers to it
numbers = []
for i in range(10):
    num = float(input("Please enter a number: "))
    numbers.append(num)

# find the total of all the numbers and print the result
sum =  sum(numbers)

# find the index of the maximum and print the result
max_index = numbers.index(max(numbers))
print(max_index)

# fnd the index of the minimum and print the result.
min_index = numbers.index(min(numbers))
print(min_index)

# calculate the average of the numbers and round off to 2 decimal places and print the result
# I will import the statistics function here to be able to use mean() to find the average
# from the class example, to be able to round off to 2 decimal places: print(round(long_number,2))
average = statistics.mean(numbers)
print(round(average,2))

# find the median number and print the result
median = statistics.median(numbers)
print(median)




