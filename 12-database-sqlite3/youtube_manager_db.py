import sqlite3

con = sqlite3.connect("youtube_manager.db")
cursor = con.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        title TEXT
    )"""
)


def list_all_videos():
    videos = cursor.execute("SELECT * FROM videos").fetchall()
    if not videos:
        print("No videos found")
    else:
        print("\nList of all videos:")
        for video in videos:
            print(f"Video ID: {video[0]}, Title: {video[1]}")


def add_video():
    video = (None, input("Enter the video title: "))
    cursor.execute("INSERT INTO videos VALUES (?, ?)", video)
    con.commit()
    print("Video added successfully")


def update_video():
    video_id = int(input("Enter the video ID to update: "))

    existing_video = cursor.execute(
        "SELECT * FROM videos WHERE id = ?", (video_id,)
    ).fetchone()
    if not existing_video:
        print("Video not found")
        return

    video = (input("Enter the new video title: "), video_id)
    cursor.execute("UPDATE videos SET title = ? WHERE id = ?", video)
    con.commit()
    print("Video updated successfully")


def delete_video():
    video_id = int(input("Enter the video ID to delete: "))
    existing_video = cursor.execute(
        "SELECT * FROM videos WHERE id = ?", (video_id,)
    ).fetchone()
    if not existing_video:
        print("Video not found")
        return

    confirm = input("Are you sure you want to delete this video? (y/n): ")
    if confirm.lower() == "y":
        cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
        con.commit()
        print("Video deleted successfully")
    else:
        print("Returning to the main menu...")


def main():
    print("Welcome to the Youtube Manager!")
    while True:
        print("\nYoutube Manager ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("\nEnter your choice: ")
        match choice:
            case "1":
                list_all_videos()
            case "2":
                add_video()
            case "3":
                update_video()
            case "4":
                delete_video()
            case "5":
                confirm = input("Are you sure you want to exit? (y/n): ")
                if confirm.lower() == "y":
                    print("Exiting...")
                    break
                else:
                    print("Returning to the main menu...")
            case _:
                print("Invalid choice")

    con.close()


if __name__ == "__main__":
    main()
