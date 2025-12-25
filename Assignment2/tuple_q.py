# You cannot modify the elements of a tuple after it is created because tuples are immutable.

# Access the second-to-last element in a tuple using negative indexing
t = (10, 20, 30, 40)
second_last = t[-2]

# Difference between list and tuple:
# List is mutable (can be changed), tuple is immutable (cannot be changed)
lst = [1, 2, 3]
tpl = (1, 2, 3)

# Change value 3 to 100 in tuple t = (1, 2, 3, 4) by converting to list and back
t = (1, 2, 3, 4)
temp = list(t)
temp[2] = 100
t = tuple(temp)

# Function to return the sum of all elements in a tuple
def sum_of_tuple(t):
    total = 0
    for num in t:
        total += num
    return total
