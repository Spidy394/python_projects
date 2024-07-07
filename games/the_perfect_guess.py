import pyttsx3
import random

def main(): 
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    a = random.randint(1, 100)
    guess_count = 1
    greetings = "Welcome to the Perfect guess game"
    print(f"|| {greetings} ||")
    engine.say(greetings)
    while True: 
        n = int(input("Make your guess: "))
        if (a > n):
            print("Higher number please: ")
            guess_count += 1 
        elif (a < n) :
            print("Lower number please")
            guess_count += 1
        else:
            break

    print(f"Bingo! You have guessed it right in {guess_count} tries!")