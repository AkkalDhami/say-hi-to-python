"""
A scope is the region where a variable is accessible.

Python follows the LEGB Rule:

L → Local
E → Enclosing
G → Global
B → Built-in

- Exists during program execution.
- Uses the LEGB rule.
- Defines where variables can be accessed.

"""


def greet():
    message = "Hello"
    print(message)


greet()

username = "akkal_dhami"


def func():
    username = "akkal"
    print(username)


print(username)
func()


x = 10


def func2(y):
    z = x + y
    return z


result = func2(1)
print(result)


def func3():
    global x
    x = 12


func3()
print(x)


def f1():
    x = 88

    def f2():
        print(x)

    return f2


myResult = f1()
myResult()


def chaicoder(num):
    def actual(x):
        return x**num

    return actual


f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(3))
