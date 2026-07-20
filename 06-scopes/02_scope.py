count = 10


def increment():
    global count
    print(count)
    count += 1


increment()
print(count)

x = "global"


def outer():
    x = "outer"

    def inner():
        x = "inner"
        print(x)

    inner()
    print(x)


outer()
print(x)
