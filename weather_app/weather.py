import requests

city = input("Enter city: ")
url = f"https://api.weatherapi.com/v1/current.json?key=[APIKEY]&q={city}"

def fetch_weather():
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
       temp = data["current"]["temp_c"]
       return temp
    else:
        raise Exception("Failed to fetch user data")
    
def main():
    try:
        temp = fetch_weather()
        print(f"The current temp is {city} is: {temp} ⁰C")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()