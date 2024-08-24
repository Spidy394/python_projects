import webbrowser
import speech_recognition as sr 
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis!")
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            # r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print(command)
        except sr.UnknownValueError:
            print("could not understand audio")