# Q1: How does the map() function work in Python? Give an example where you square each number in a list.
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, nums))
print(squared)   # [1, 4, 9, 16]

# Q2: What is the output of the following code?
from functools import reduce
result = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(result)    # Output: 24

# Q3: How would you use the map() function to convert all string elements of a list to uppercase?
words = ["python", "map", "reduce"]
upper_words = list(map(lambda x: x.upper(), words))
print(upper_words)   # ['PYTHON', 'MAP', 'REDUCE']

# Q4: Write a Python program that uses reduce() to find the GCD of a list of numbers.
from functools import reduce
import math

nums = [24, 36, 60]
gcd_result = reduce(math.gcd, nums)
print(gcd_result)    # 12

# Q5: Compare and contrast the map() and filter() functions in Python.
# map() applies a function to each element and returns transformed values
# filter() applies a condition and returns only elements that satisfy it
nums = [1, 2, 3, 4, 5]
mapped = list(map(lambda x: x * 2, nums))        # [2, 4, 6, 8, 10]
filtered = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]
