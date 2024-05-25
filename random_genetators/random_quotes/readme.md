# Random Quote Fetcher 📝✨

Welcome to the Random Quote Fetcher project! This Python script fetches random quotes from the FreeAPI and displays them in the console. It's a fun way to get inspired by random quotes!

## How It Works 🔧

The script uses the `requests` library to make an API call to the FreeAPI to fetch a random quote. The quote and its author are then displayed in the console. You can choose to fetch another quote or exit the program.

## Code Explanation 🧐

### `fetch_random_quotes()` Function

This function fetches a random quote from the FreeAPI.

- The function sends a GET request to the API endpoint.

- It parses the JSON response to extract the quote and its author.

- If the request is successful, it returns the quote and author. Otherwise, it raises an exception.

### `main()` Function

This function manages the flow of the program, allowing the user to fetch multiple quotes or exit.

- It enters an infinite loop to continually fetch quotes until the user decides to stop.

- It handles exceptions that may occur during the API call.

- It prompts the user to fetch another quote or exit.

## Running the Script ▶️

1. Install Dependencies:

	```bash
	pip install requests
	```

1. Run the Script:

	```bash
	python your_script.py
	```

## Example Output 🎉

```md
******************************************************************************************************************************************************
Your limitation—it's only your imagination.
					by Unknown

******************************************************************************************************************************************************
Want another quote? (y/n): y
```

## Features ✨

- Fetches random quotes from the FreeAPI.

- Displays quotes in a formatted manner.

- Allows user to fetch multiple quotes.

### ℹ If you have suggestions or improvements, feel free to open an issue or submit a pull request.

---