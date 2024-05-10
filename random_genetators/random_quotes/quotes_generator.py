import requests

def fetch_random_quotes():
    url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        quote = data["data"]["content"]
        author = data["data"]["author"]
        return quote, author
    raise Exception("Failed to fetch quote")

def main():
    while True:
        try:
            quote, author = fetch_random_quotes()
            print(f"{"*" * 150} \n{quote} \n\t\t\t\t\tby {author} \n\n{"*" * 150}")
            repeat = input("Want another joke? (y/n): ")
            if repeat.lower() != 'y':
                print("Thank you! Have a great day!")
                break
        except Exception as e:
            print(str(e))

if __name__ == "__main__":
    main()