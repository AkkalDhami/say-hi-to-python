from lib.utils import (
    list_all_todos,
    add_todo,
    mark_todo_as_completed,
    delete_todo,
    mark_todo_as_uncompleted,
)


def main():
    while True:
        print("\nWelcome to Todo CLI!")
        print("1. List all todos")
        print("2. Add a new todo")
        print("3. Mark a todo as completed")
        print("4. Mark a todo as uncompleted")
        print("5. Delete a todo")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                list_all_todos()
            case 2:
                add_todo()
            case 3:
                mark_todo_as_completed()
            case 4:
                mark_todo_as_uncompleted()
            case 5:
                delete_todo()
            case 6:
                print("Exiting Todo CLI...")
                exit()
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
