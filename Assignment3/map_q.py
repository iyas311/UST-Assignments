# Q1: Write a Python program using map() to convert a list of integers into their squares.
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, nums))
print(squares)

# Q2: Write a program using map() to convert all strings in a list to uppercase.
words = ["python", "map", "function"]
upper_words = list(map(lambda x: x.upper(), words))
print(upper_words)

# Q3: Given a list of temperatures in Celsius, use map() to convert them to Fahrenheit.
celsius = [0, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)

# Q4: Write a program using map() to calculate the length of each word in a list of strings.
words = ["python", "coding", "map"]
lengths = list(map(len, words))
print(lengths)

# Q5: Use map() to add 10 to each element of a given list of numbers.
nums = [5, 10, 15]
added = list(map(lambda x: x + 10, nums))
print(added)
