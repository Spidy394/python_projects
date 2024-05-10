import requests


def fetch_random_joke():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        content = data["data"]["content"]
        return content
    else:
        raise Exception("Failed to fetch joke")

def main():
    while True:
        try:
            content = fetch_random_joke()
            print(f"{"*" * 150} \n{content} \n\n{"*" * 150}")
            repeat = input("Want another joke? (y/n): ")
            if repeat.lower() != 'y':
                print("Thank you! Have a great day!")
                break
        except Exception as e:
            print(str(e))

if __name__ == "__main__":
    main()