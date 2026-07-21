"""

Problem 05: Write a function that greets a user. If no name is provided, it should greet with a default name

"""


def greets(greet="Hello", name="Akkal"):
    return f"{greet}! {name}"


print(greets("Hi", "Akkal Dhami"))
