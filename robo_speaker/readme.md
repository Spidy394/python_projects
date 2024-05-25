# 📌 🤖 Robo Speaker 🗣

Welcome to Robo Speaker! This Python program uses the `pyttsx3` library to convert text input into speech. You can type any text, and the robo speaker will speak it aloud.

## Features 🚀

- 🔊 Converts text input into speech

- 🗣️ Real-time text-to-speech conversion

- 👋 Exit the program gracefully by typing "bye"

## Setup ⚙️

1. Ensure you have Python 3 installed.

1. Install the `pyttsx3` library

        pip install pyttsx3

1. Clone the repository or download the robo_speaker.py file.

## Usage ℹ️

1. Run the program using Python 3:

        python robo_speaker.py

1. Enter the text you want the robo speaker to speak.

1. Type "bye" to exit the program.

## How It Works 🧐

- The program initializes the `pyttsx3` engine.

- It sets the speech rate to 150 words per minute.

- It enters an infinite loop where it waits for the user to input text.

- The input text is then spoken by the robo speaker.

- If the user types "bye", the program says "Goodbye!" and exits.

## Example Output 🎉

```
|| Welcome To Robo Speaker ||
Enter what you want robo to speak: Hello, world!
(Hello, world! is spoken aloud)
|| Welcome To Robo Speaker ||
Enter what you want robo to speak: This is a test.
(This is a test. is spoken aloud)
|| Welcome To Robo Speaker ||
Enter what you want robo to speak: bye
(Goodbye! is spoken aloud)
Goodbye!
```

---