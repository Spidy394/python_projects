from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://<username>:<password>@cluster0.ottb3zo.mongodb.net/")

db = client["ytmanager"]
video_collection = db["videos"]

def repetaion(f):
    while True:
        choice = input("Repeat? ")
        if choice.lower() == 'y':
            f()
        elif choice.lower() == 'n':
            break
        else:
            print("Invalid")

def list_videos():
    for video in video_collection.find():
        print(f"Id: {video['_id']}, Name: {video['name']}, Time: {video['time']}, Link: {video['link']}")

def add_videos():
    name = input("Enter the video name: ")
    time = input("Enter the video time: ")
    link = input("Enter video link: ")
    video_collection.insert_one({"name": name, "time": time, "link": link})
    list_videos()

def update_video(name, time, link):
    video_id = input("Enter video id to update: ")
    new_name = input("Enter the video name: ")
    new_time = input("Enter the video time: ")
    new_link = input("Enter link: ")
    video_collection.update_one({'id': ObjectId(video_id)}, {"$set": {"name": new_name}, "time": new_time, "link": new_link})
    list_videos()

def delete_video():
    video_id = input("Enter video id to delete: ")
    video_collection.delete_one({"_id": ObjectId(video_id)})
    list_videos()

def main():
    while True:
        print("\n YouTube Manager App with MongoDB")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit app")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_videos()
            case '2':
                add_videos()
                repetaion(add_videos)
            case '3':
                list_videos()
                update_video()
                repetaion(update_video)
            case '4':
                list_videos()
                delete_video()
                repetaion(delete_video)
            case '5':
                print("Thanks You!!")
                break
            case _:
                print("Invalid Choice!!")

if __name__ == "__main__":
    main()