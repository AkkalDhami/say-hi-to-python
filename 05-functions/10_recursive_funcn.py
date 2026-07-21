"""

Problem 10: Create a recursive function to calculate the factorial of a number.

"""


def factorial(num):
    if num < 0:
        return "Invalid num"
    if num < 1:
        return 1
    else:
        return factorial(num - 1) * num


print(factorial(0))
