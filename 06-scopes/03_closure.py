"""

A closure is a function that remembers variables from its enclosing scope, even after the enclosing function has finished executing.

- Create function factories.
- Maintain private state without using classes.
- Write decorators.
- Build callbacks.

"""


def outer():
    message = "Hello"

    def inner():
        print(message)

    return inner


greet = outer()

greet()


def multiplier(n):

    def multiply(x):
        return x * n

    return multiply


double = multiplier(2)
triple = multiplier(3)

print(double(10))
print(triple(10))
