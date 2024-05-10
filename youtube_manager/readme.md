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
        "link": "https://www.youtube.com/watch?v=video1"
    },
    {
        "name": "Video 2",
        "time": "05:45",
        "link": "https://www.youtube.com/watch?v=video2"
    }
]
```

---
