# 📌 YouTube Video Manager 🎥

This Python program allows users to manage a list of YouTube videos. Users can add, update, delete, and list all videos stored in a JSON file. The program provides a simple command-line interface for interacting with the video manager.

## Features 🚀

- 📋 List all YouTube videos
- ➕ Add a new YouTube video
- ✏️ Update details of an existing video
- ❌ Delete a video
- 💾 Save data to a JSON file (`youtube.txt`)

## Usage 🛠️

1. Clone the repository or download the `youtube_manager.py` file.

1. Run the program using Python 3:

    ```bash
    python youtube_manager.py
    ```

1. Choose from the menu options to manage your YouTube videos.

## Menu Options 📑

1. **List all YouTube videos:** Displays a list of all stored videos with their names, durations, and links.

1. **Add a YouTube video:** Allows the user to input details for a new video and adds it to the list.

1. **Update a YouTube video details:** Prompts the user to select a video to update and enter new details.

1. **Delete a YouTube video:** Lets the user choose a video to delete from the list.

1. **Exit the app:** Terminates the program.

## JSON File 📄

The program uses a JSON file (`youtube.txt`) to store the list of videos. If the file does not exist, it will be created automatically. Each video is stored as a dictionary with keys for name, time, and link.

Example JSON format:

```json
[
    {
        "name": "Video 1",
        "time": "10:30",
        "link": "https://youtu.be/BBJa32lCaaY?si=3R9CjMHQV676YKNf"
    },
    {
        "name": "Video 2",
        "time": "05:45",
        "link": "https://youtu.be/BBJa32lCaaY?si=3R9CjMHQV676YKNf"
    }
]
```

---

# 📌 YouTube Video Manager 🎥 with SQLITE3 🗂️

This Python program is a YouTube video manager app that uses SQLite3 to store video details. Users can list, add, update, and delete videos using a command-line interface.

## Features 🚀

- 📋 List all YouTube videos

- ➕ Add a new YouTube video

- ✏️ Update details of an existing video

- ❌ Delete a video

- 💾 Save data to a SQLite database (`youtube_videos.db`)

## Setup ⚙️

1. Ensure you have Python 3 installed.

1. Clone the repository or download the `youtube_manager_with_db.py` file.

## Usage ℹ️

1. Run the program using Python 3:

    ```bash
        python youtube_manager.py
    ```

1. Choose from the menu options to manage your YouTube videos.

## Menu Options 📑

1. **List videos:** Displays a list of all stored videos with their names, durations, and links.

1. **Add video:** Allows the user to input details for a new video and adds it to the list.

1. **Update video:** Prompts the user to select a video to update and enter new details.

1. **Delete video:** Lets the user choose a video to delete from the list.

1. **Exit app:** Terminates the program.

## Database Schema 🗃️

The program uses a SQLite database (`youtube_videos.db`) to store the list of videos. The videos table schema is as follows:

- `id` INTEGER PRIMARY KEY

- `name` TEXT NOT NULL

- `time` TEXT NOT NULL

- `link` TEXT NOT NULL

## Sample Run 📝

```
YouTube manager app with SQLITE3
1. List videos
2. Add video
3. Update video
4. Delete video
5. Exit app
Enter your choice: 2

Enter video name: My Video
Enter duration: 10:00
Enter link: https://youtu.be/BBJa32lCaaY?si=3R9CjMHQV676YKNf
Video added!
Do you want to add another video(y/n): n

1. List videos
2. Add video
3. Update video
4. Delete video
5. Exit app
Enter your choice: 1

(1, 'My Video', '10:00', 'https://youtu.be/BBJa32lCaaY?si=3R9CjMHQV676YKNf')

1. List videos
2. Add video
3. Update video
4. Delete video
5. Exit app
Enter your choice: 5

Thank you, have a great day!
```

---
