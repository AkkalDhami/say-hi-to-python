"""

Problem 01: Write a decorator that measures the time a function takes to execute.

"""

import time


def boilerplate(func):
    def wrapper(*args):
        print("Hello")
        return func(*args)

    return wrapper


def timer(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()

        print(
            f"func: {func.__name__} ran in {round((end_time - start_time), 2)}s time."
        )
        return result

    return wrapper


@boilerplate
@timer
def test(n):
    time.sleep(n)


test(2)
