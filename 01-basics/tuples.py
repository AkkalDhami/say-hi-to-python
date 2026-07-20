"""
list => mutable
tuple => immutable
"""

user = ("akkal", "dhami", 20)
print(user)
print(user[0])

# user[0] = "akkal dhami" #! ERROR because tuple is immutable

print("\ntype: ", type(user))
print("length: ", len(user))
print("index: ", user.index("dhami"))
print("count: ", user.count("akkal"))

user_list = list(user)
user_list[0] = "akkal dhami"
user = tuple(user_list)

print("\nupdated user: ", user)

if("akkal dhami" in user):
  print("akkal dhami is in user")


test = (1, 2, 3)
print("\ntest: ", test)
del test
# print("test: ", test) #! ERROR: NameError: name 'test' is not defined


# ? unpacking => destructuring
# name, email, age = user
#  or 
(name, email, age) = user

print("\nname: ", name)
print("email: ", email)
print("age: ", age)


nums = (1, 2, 3, 4, 5, 6, 7)
(a, b, *rest, e) = nums

print("\na: ", a)
print("b: ", b)
print("e: ", e)
print("rest: ", rest)