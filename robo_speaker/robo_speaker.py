import pyttsx3

def main():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    while True:
        print("|| Welcome To Robo Speaker ||")
        text = input("Enter what you want robo to speak: ")

        if text.lower() == 'bye':
            engine.say("Goodbye!")
            engine.runAndWait()
            print("Goodbye!")
            break

        engine.say(text)
        engine.runAndWait()

if __name__ == "__main__":
    main()