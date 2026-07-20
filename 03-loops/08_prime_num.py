"""

Problem 08: Check if a number is prime.

"""

num = int(input("Enter a number: "))

def is_prime(num):

    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


if is_prime(num):
    print(f"{num} is a prime number")

else:
    print(f"{num} is not a prime number")
