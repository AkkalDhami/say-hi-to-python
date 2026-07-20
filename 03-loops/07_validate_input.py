"""

Problem 07: Keep asking the user for input until they enter a number between 1 and 10.

"""

num = int(input("Enter a number: "))

while num < 1 or num > 10:
    print("Invalid input. Please enter a number between 1 and 10.")
    num = int(input("Enter a number: "))
