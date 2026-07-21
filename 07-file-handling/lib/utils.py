from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

DATA_DIR.mkdir(exist_ok=True)  # Creates the folder if it doesn't exist


def read_file_and_folders():

    files = [f for f in DATA_DIR.iterdir() if f.is_file()]

    print("\nAvailable Files:\n")
    for i, file in enumerate(files):
        print(f"{i + 1}. {file.name}")


def create_file():
    read_file_and_folders()
    try:
        filename = input("\nEnter file name: ")
        file = DATA_DIR / filename
        if file.exists():
            print("\nFile aready exists.\n")
            return
        with open(file, "w") as fs:
            data = input("Enter a content:\n")
            fs.write(data)
        print(f"\nFile: {filename} created successfully.\n")
    except Exception as err:
        print(f"An Error occured: {err}")


def read_file():
    read_file_and_folders()
    try:
        filename = input("\nEnter file name: ")
        file = DATA_DIR / filename
        if not file.exists() or not file.is_file():
            print("\nFile doesnot exists.\n")
            return
        print("\nFile content:")
        print(file.read_text())
        # with open(file) as fs:
        #     data = fs.read()
        #     print(data)

        print("\nFile read successfully.\n")
    except Exception as err:
        print(f"An Error occured: {err}")


def update_file():
    read_file_and_folders()
    try:
        filename = input("\nEnter file name: ")
        old_file = DATA_DIR / filename
        if not old_file.exists() or not old_file.is_file():
            print("\nFile doesnot exists.\n")
            return

        print("\n1. Change file name")
        print("2. Overwrite file content")
        print("3. Append file content")

        response = int(input("\nSelect an option(1-3):"))

        if response == 3:
            with open(old_file, "a") as fs:
                data = input("Enter content:\n")
                fs.write("\n" + data)
            print("\nFile content updated successfully.\n")

        if response == 2:
            with open(old_file, "w") as fs:
                data = input("Enter content:\n")
                fs.write(data)
            print("\nFile content overwritten successfully.\n")

        if response == 1:
            new_name = input("Enter file new name: ")

            new_file = DATA_DIR / new_name
            if new_file.exists():
                print(f"'{new_name}' already exists.")
                return

            old_file.rename(new_file)
            print("\nFile renamed successfully.\n")

    except Exception as err:
        print(f"An Error occured: {err}")


def delete_file():
    read_file_and_folders()
    try:
        filename = input("\nEnter file name: ")
        file = DATA_DIR / filename

        if not file.exists():
            print("File not found!")
            return

        confirm = input(f"Are you sure you want to delete '{filename}'? (y/n): ")

        if confirm.lower() == "y":
            file.unlink()
            print("\nFile deleted successfully.\n")
        else:
            print("\nDeletion cancelled.\n")
    except Exception as err:
        print(f"An Error occured: {err}")
