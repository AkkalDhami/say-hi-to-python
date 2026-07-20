"""

Problem 02: Calculate the sum of even numbers up to a given number n.

"""

n = int(input("Enter a number: "))

sum = 0

for i in range(2, n + 1, 2):
    sum += i

print("Sum of even numbers up to", n, "is:", sum)
