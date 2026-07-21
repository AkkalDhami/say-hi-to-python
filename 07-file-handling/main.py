from lib.utils import create_file, delete_file, read_file, update_file


def display():
    print("\n1. Create a file")
    print("2. Read a file")
    print("3. Update a file")
    print("4. Delete a file")


display()
option = int(input("\nSelect an option (1-5): "))

if option == 1:
    create_file()

elif option == 2:
    read_file()

elif option == 3:
    update_file()

elif option == 4:
    delete_file()
