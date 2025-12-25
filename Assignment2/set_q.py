# Q1: How do you remove all elements from a set in Python?
s = {1, 2, 3}
s.clear()

# Q2: What is the output of the following code snippet?
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a - b)    # Output: {1, 2}

# Q3: How do you check if an element is present in a set?
s = {10, 20, 30}
is_present = 20 in s

# Q4: Write a Python program to find the intersection of two sets.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection = set1 & set2
print(intersection)   # {3, 4}

# Q5: How does a set handle duplicate values when adding them?
s = {1, 2, 3}
s.add(2)    # Duplicate value is ignored, set remains unchanged
