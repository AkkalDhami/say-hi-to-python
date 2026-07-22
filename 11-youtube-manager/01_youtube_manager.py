import json

FILE_NAME = "youtube.json"


def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data(videos):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(videos, file, indent=2)
    except Exception as e:
        print(f"Error saving data: {e}")


def list_all_videos(videos):
    print("\nList of all videos:")
    for i, video in enumerate(videos, start=1):
        print(f"{i}. Video ID: {video['id']}, Title: {video['title']}")


def add_video(videos):
    video = {"id": len(videos) + 1, "title": input("Enter the video title: ")}
    videos.append(video)
    save_data(videos)
    print("Video added successfully")


def update_video(videos):
    video_id = int(input("Enter the video ID to update: "))
    for video in videos:
        if video["id"] == video_id:
            video["title"] = input("Enter the new video title: ")
            save_data(videos)
            print("Video updated successfully")
            return
    else:
        print("Video not found")


def delete_video(videos):
    video_id = int(input("Enter the video ID to delete: "))
    confirm = input("Are you sure you want to delete this video? (y/n): ")
    if confirm.lower() == "y":
        for video in videos:
            if video["id"] == video_id:
                videos.remove(video)
                save_data(videos)
                print("Video deleted successfully")
                return
        else:
            print("Video not found")


def main():
    videos = load_data()
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
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                confirm = input("Are you sure you want to exit? (y/n): ")
                if confirm.lower() == "y":
                    print("Exiting...")
                    break
                else:
                    print("Returning to the main menu...")
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()
