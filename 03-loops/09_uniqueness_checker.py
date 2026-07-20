"""

Problem 09: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

"""

items = ["apple", "banana", "orange", "apple", "mango"]

# ? method 1:

print("\nmethod 1: ")

for item in items:
    if items.count(item) == 1:
        print(f"{item} is unique")
    else:
        print(f"{item} is not unique")


# ? method 2:

print("\nmethod 2: ")
unique_items = set()

for item in items:
    if item in unique_items:
        print(f"{item} is not unique")
        break
    unique_items.add(item)
