# Q1: Write a Python program using filter() to extract all even numbers from a list.
nums = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# Q2: Write a program using filter() to select all words from a list that start with a vowel.
words = ["apple", "banana", "orange", "umbrella", "grape"]
vowel_words = list(filter(lambda w: w[0].lower() in "aeiou", words))
print(vowel_words)

# Q3: Given a list of integers, use filter() to remove all negative numbers.
nums = [-10, -5, 0, 5, 10, 15]
non_negative = list(filter(lambda x: x >= 0, nums))
print(non_negative)

# Q4: Write a program using filter() to find numbers greater than 50 from a list.
nums = [10, 45, 60, 80, 30, 100]
greater_than_50 = list(filter(lambda x: x > 50, nums))
print(greater_than_50)

# Q5: Use filter() to extract all palindromic strings from a list.
words = ["madam", "python", "level", "code", "radar"]
palindromes = list(filter(lambda w: w == w[::-1], words))
print(palindromes)
