import requests

def fetch_random_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        if data["type"] == "twopart":
            setup = data["setup"]
            delivery = data["delivery"]
            print(f"{"*" * 150} \n{setup} \n\nn
                {delivery} \n\n{"*" * 150}")
        else:
            joke = data["joke"]
            print(f"{"*" * 150} \n{joke} \n\n{"*" * 150}")
    else:
        print(f"Failed to fetch joke.")


def main():
    while True:
        try:
            fetch_random_joke()
            repeat = input("Want another joke? (y/n): ")
            if repeat.lower() == 'n':
                print("Thank you! Have a great day!")
                break
        except Exception as e:
            print(str(e))

if __name__ == "__main__":
    main()