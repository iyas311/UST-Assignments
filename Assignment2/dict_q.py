# Q1: How can you add a new key-value pair to an existing dictionary in Python?
d = {"a": 10, "b": 20}
d["c"] = 30

# Q2: What happens if you try to access a key that does not exist in a dictionary?
d = {"x": 1}
# print(d["y"])        # Raises KeyError
value = d.get("y")     # Returns None instead of error

# Q3: Write a Python function that takes a dictionary and returns a list of keys that have values greater than 50.
def keys_greater_than_50(d):
    result = []
    for key, value in d.items():
        if value > 50:
            result.append(key)
    return result

# Q4: How would you iterate over both keys and values of a dictionary in Python?
d = {"a": 10, "b": 20, "c": 30}
for key, value in d.items():
    print(key, value)

# Q5: Write a Python function that merges two dictionaries.
def merge_dicts(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged
