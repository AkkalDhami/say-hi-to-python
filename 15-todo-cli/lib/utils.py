import sqlite3

con = sqlite3.connect("db/todo.db")
cursor = con.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        title TEXT,
        completed BOOLEAN DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )"""
)


def list_all_todos():
    todos = cursor.execute("SELECT * FROM todos").fetchall()
    if not todos:
        print("No todos found")
    else:
        print("\nList of all todos:")
        for todo in todos:
            print(
                f"Todo ID: {todo[0]}, Title: {todo[1]}, Completed: {todo[2]}, Created At: {todo[3]}"
            )


def add_todo():
    title = (input("Enter title: "),)
    cursor.execute("INSERT INTO todos (title) VALUES (?)", title)
    con.commit()
    print("Todo added successfully")


def mark_todo_as_completed():
    try:
        todo_id = int(input("Enter the Todo ID to update: "))
        existing_todo = cursor.execute(
            "SELECT * FROM todos WHERE id = ?", (todo_id,)
        ).fetchone()
        if not existing_todo:
            print("Todo not found")
            return
        cursor.execute("UPDATE todos SET completed = ? WHERE id = ?", (1, todo_id))
        print("Todo marked as completed successfully")
    except Exception as e:
        print(f"Error updating todo: {e}")


def mark_todo_as_uncompleted():
    try:
        todo_id = int(input("Enter the Todo ID to update: "))
        existing_todo = cursor.execute(
            "SELECT * FROM todos WHERE id = ?", (todo_id,)
        ).fetchone()
        if not existing_todo:
            print("Todo not found")
            return
        cursor.execute("UPDATE todos SET completed = ? WHERE id = ?", (0, todo_id))
        print("Todo marked as uncompleted successfully")
    except Exception as e:
        print(f"Error updating todo: {e}")


def delete_todo():
    todo_id = int(input("Enter the Todo ID to delete: "))
    existing_todo = cursor.execute(
        "SELECT * FROM todos WHERE id = ?", (todo_id,)
    ).fetchone()
    if not existing_todo:
        print("Todo not found")
        return
    confirm = input("Are you sure you want to delete this todo? (y/n): ")
    if confirm.lower() == "y":
        cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
        con.commit()
        print("Todo deleted successfully")
    else:
        print("Returning to the main menu...")
