import json

main_file = 'youtube.txt'

def load_data():
    try:
        with open(main_file, 'r') as file:
            test = json.load(file)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open(main_file, 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n" + "*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}, Link: {video['link']}")
    print("\n" + "*" * 70)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video length: ")
    link = input("Enter link: ")
    videos.append({'name': name, 'time': time, 'link': link})
    save_data_helper(videos)
    print("Video saved!")

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video lenght: ")
        link = input("Enter new video link: ")
        videos[index-1] = {'name':name, 'time':time, 'link':link}
        save_data_helper(videos)
        print("Video updated!")
    else:
        print("Invalid index selected!!")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("Video deleted!")
    else:
        print("Invalid video index selected!!")

def main():
    videos = load_data()
    while True:
        print("\n YouTube Manager | Choose an option")
        print("1. List all YouTube videos ")
        print("2. Add a YouTube video ")
        print("3. Update a YouTube video details ")
        print("4. Delete a YouTube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
                while True:
                    repeat = input("Do you want to add another video(y/n): ")
                    if repeat.lower() == 'y':
                        add_video(videos)
                    elif repeat.lower() == 'n':
                        break
                    else:
                        print("Invalid choice!")
            case '3':
                update_video(videos)
                while True:
                    if videos != []:
                        repeat = input("Do you want to update another video(y/n): ")
                        if repeat.lower() == 'y':
                            update_video(videos)
                        elif repeat.lower() == 'n':
                            break
                        else:
                            print("Invalid choice!")
                    else:
                        print("No videos to update!")
                        break
            case '4':
                delete_video(videos)
                while True:
                    if videos != []:
                        repeat = input("Do you want to delete another video(y/n): ")
                        if repeat.lower() == 'y':
                            delete_video(videos)
                        elif repeat.lower() == 'n':
                            break
                        else:
                            print("Invalid choice!")
                    else:
                        print("No videos to delete!")
                        break
            case '5':
                print("Thank you, Have a nice day!")
                break
            case _:
                print("Invalid Choice!!")

if __name__ == "__main__":
    main()