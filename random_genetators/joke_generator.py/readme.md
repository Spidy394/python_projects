# 🤣 Random Joke Fetcher 🃏

Welcome to the Random Joke Fetcher! This Python script fetches random jokes from the [FreeAPI](https://freeapi.app/) and displays them in the console. Get ready for some laughs!

## Features 🚀

- 😂 Fetches random jokes from the FreeAPI

- 📜 Displays jokes in formatted manner.

- 🔄 Allows fetching multiple jokes or exiting the program

## Setup ⚙️

1. Ensure you have Python 3 installed. 

1. Install the `requests` library:

        pip install resquets

1. Clone the repository or download the `jokes_freeapi.py` file.

## Usage ℹ️

1. Run the program using python 3:

        python jokes_freeapi.py

1. Enjoy the jokes! You can choose to fetch another joke or exit the program.

## How It Works 🧐

- The program uses the `requests` library to make an API call to the FreeAPI.

- It fetches a random joke and displays it in the console.

- You can choose to fetch another joke by typing "y" or exit the program by typing "n".

## Example Output 🎉

        ******************************************************************************************************************************************************
        Why don't scientists trust atoms? Because they make up everything!
        ******************************************************************************************************************************************************
        Want another joke? (y/n): y
        ******************************************************************************************************************************************************
        What do you call fake spaghetti? An impasta!
        ******************************************************************************************************************************************************
        Want another joke? (y/n): n
        Thank you! Have a great day!

---

# 🤣 Random Joke Fetcher v2 🃏

Welcome to the Random Joke Fetcher! This Python script fetches random jokes from the [JokeAPI](https://jokeapi.dev) and displays them in the console. Get ready for some laughs!

## Features 🚀

- 😂 Fetches random jokes from the JokeAPI

- 📜 Displays both single-part and two-part jokes in a formatted manner

- 🔄 Allows fetching multiple jokes or exiting the program

## Setup ⚙️

1. Ensure you have Python 3 installed.

1. Install the `requests` library:

        pip install requests

1. Clone the repository or download the `jokes_jokeapi.py` file.

        python jokes_jokeapi.py

1. Enjoy the jokes! You can choose to fetch another joke or exit the program.

## How It Works 🧐

- The program uses the requests library to make an API call to the JokeAPI.

- It fetches a random joke and displays it in the console.

    - If the joke is a two-part joke, it displays the setup and delivery.
    
    - If the joke is a single-part joke, it displays the joke.

- You can choose to fetch another joke by typing "y" or exit the program by typing "n".

## Example Output 🎉

        ******************************************************************************************************************************************************
        Why don't scientists trust atoms?

        Because they make up everything!
        ******************************************************************************************************************************************************
        Want another joke? (y/n): y
        ******************************************************************************************************************************************************
        What do you call fake spaghetti? An impasta!
        ******************************************************************************************************************************************************
        Want another joke? (y/n): n
        Thank you! Have a great day!

---