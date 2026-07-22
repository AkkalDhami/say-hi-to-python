user = {
    "id": 1,
    "name": "akkal",
    "age": 20,
    "email": "akkal@gmail.com",
    "is_active": True,
    "is_admin": False,
    "session_id": "x-session-id",
}

print(user)
print("name: ", user["name"])
print("age: ", user.get("age"))

user["age"] = 21
print("updated age: ", user["age"])

print("\nkeys: ", user.keys())  # [key]
print("\nvalues: ", user.values())  # [value]
print("\nitems: ", user.items())  # [(key, value)]

print("\nfor in: ")
for key, value in user.items():
    print(key, ": ", value)

print("\n")
for u in user:
    print(u, "=> ", user[u])

print("\nis active: ", "email" in user)
if "email" in user:
    print("email exists")

print("length: ", len(user))

print("\npop: ", user.pop("session_id"))
print("user after pop: ", user)

user2 = {
    "name": "akkal dhami",
    "email": "akkal_dhami@gmail.com",
    "age": 2,
    "is_active": True,
}
print("\nuser2: ", user2)
print("pop_item: ", user2.popitem())  # * removes last item
print("user2 after popitem: ", user2)

del user2["age"]
print("\nuser2 after del: ", user2)

user3 = {
    "name": "akkal dhami",
    "email": "akkal_dhami@gmail.com",
    "age": 2,
    "address": {"city": "kathmandu", "zip": "12345"},
}

print("\nuser3: ", user3)

print("\nuser3->address: ", user3["address"])
print("\nuser3->address->city: ", user3["address"]["city"])

copied_user = user3.copy()
print("\ncopied user: ", copied_user)

user3.clear()
print("\nuser3 after clear: ", user3)
print("\ncopied user after clear user3: ", copied_user)

squared_num = {x: x**2 for x in range(1, 11)}

print("\nsquared num: ", squared_num)

keys = ["name", "email", "age"]

default = "unknown"
# user4 = dict(zip(keys, [default] * len(keys)))
user4 = dict.fromkeys(keys, default)

print("\nuser4: ", user4)
