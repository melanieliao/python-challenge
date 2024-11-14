# @TODO: Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
if len(numbers) == 0:
    return 0

#calculate the sum of the list and divide by the numbers of elements 
return sum(numbers)_ / len(numbers)

# Test your function with the following:
# print(average([1, 5, 9]))
print(average([1, 5, 9]))
# print(average(range(11)))
print(average(range(11)))