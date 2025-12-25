# Add an element at the end of a list
lst = [1, 2, 3]
lst.append(4)

# Remove an element from a list by its index
lst = [10, 20, 30, 40]
lst.pop(2)      # removes element at index 2
# del lst[2]    # another way

# Output of the given code snippet
lst = [1, 2, 3, 4, 5]
lst[1:3] = [10, 20]
print(lst)      # [1, 10, 20, 4, 5]

# Check if an element exists in a list
lst = [5, 10, 15]
exists = 10 in lst

# Function to remove duplicates without using set()
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
