import requests
import os
from dotenv import load_dotenv

city = input("Enter city: ")

def fetch_weather():
    load_dotenv()
    url = f"https://api.weatherapi.com/v1/current.json?key={os.getenv('api_key')}&q={city}"
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