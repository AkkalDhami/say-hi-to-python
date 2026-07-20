"""

Problem 05: Given a string, find the first non-repeated character.

"""

str = input("Enter a string: ")

for char in str:
    if str.count(char) == 1:
        print("first non repeated char:", char)
        break
