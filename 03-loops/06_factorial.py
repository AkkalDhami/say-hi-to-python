"""

Problem 06: Compute the factorial of a number using a while loop.

"""

num = int(input("Enter a number: "))

org_num = num

fact = 1

while num > 0:
    fact *= num
    num -= 1

print(f"Factorial of {org_num} is {fact}")
