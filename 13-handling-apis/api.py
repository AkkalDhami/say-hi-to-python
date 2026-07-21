import requests


def fetch_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        if data["success"] and data["data"]:
            users = data["data"]
            user = {
                "id": users["id"],
                "username": users["login"]["username"],
                "name": f"{users['name']['first']} {users['name']['last']}",
                "email": users["email"],
            }
            return user
    else:
        raise Exception("Failed to fetch user data")


def main():
    try:
        user = fetch_user()
        print(user)
    except Exception as e:
        print(f"Error fetching user data: {e}")


if __name__ == "__main__":
    main()
