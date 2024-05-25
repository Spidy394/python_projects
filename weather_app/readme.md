# Weather Fetcher ☀️🌧️❄️

Welcome to the Weather Fetcher project! This Python script fetches the current weather for a specified city using the [WeatherAPI](https://chatgpt.com/c/9f8a8936-9724-42ef-ab20-decc6c9a7f8e).

## How It Works 🔧

The script uses the `requests` library to make an API call to the WeatherAPI to fetch current weather data. It then displays the current temperature in the specified city.

## Code Explanation 🧐

### `fetch_weather()` Function

This function fetches the current weather data for a specified city from the WeatherAPI.

- The function sends a GET request to the WeatherAPI endpoint with the provided API key and city.

- It parses the JSON response to extract the current temperature in Celsius.

- If the request is successful, it returns the temperature. Otherwise, it raises an exception.

### `main()` Function

This function manages the flow of the program, prompting the user to enter a city and displaying the current temperature.

- It calls the `fetch_weather()` function and prints the temperature.

- It handles exceptions that may occur during the API call.

## Running the Script ▶️

1. Install Dependencies:

        pip install requests

1. Set Up API Key:

    - Obtain your API key from [WeatherAPI](https://www.weatherapi.com/).

    - Replace `'enter your api key'` in the script with your actual API key.

1. Run the Script:

        python weather.py


1. Enter the City:

    - When prompted, enter the name of the city for which you want to fetch the weather.

## Example Output 🎉

```
Enter city: London
The current temp in London is: 15 ⁰C
```

## Features ✨

- Fetches current weather data from the WeatherAPI.

- Displays the current temperature in the specified city.

- Handles exceptions gracefully.

---