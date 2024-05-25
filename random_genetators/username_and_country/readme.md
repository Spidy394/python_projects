# Random User Fetcher 🧑‍💻🌍

This script fetches a random user from the FreeAPI service and displays their username and country. The purpose is to demonstrate how to interact with a public API using Python.

# How It Works ⚙️

1. **Fetch Random User:** The script sends a GET request to the FreeAPI endpoint to fetch a random user's details.

1. **Parse Response:** It parses the JSON response to extract the user's username and country.

1. **Display Information:** The username and country of the fetched user are printed to the console.

## Code Explanation 💡

Here's a breakdown of the code:

### 1. Importing Required Libraries 📚

```bash
import requests
```

### 2. Fetching Random User Data 🌐

The `fetch_random_user_freeapi` function sends a GET request to the FreeAPI endpoint, checks if the request was successful, and then extracts and returns the user's username and country.

### 3. Main Function 🏁

The main function calls fetch_random_user_freeapi, handles any exceptions, and prints the fetched username and country.

## Running the Script ▶️

To run the script, make sure you have Python and the `requests` library installed. Then, execute the script from the command line:

```bash
python script_name.py
```

Replace `script_name.py` with the actual name of your script file.

## Example Output 🖥️

```
Username: john_doe
Country: Wonderland
```

---