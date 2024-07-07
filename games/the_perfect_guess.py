import random
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 250)
greetings = "Welcome to the Perfect guess game"
higher = "Higher number please"
lower = "Lower number please"
repeat_message = "Do you want to play again"
bye_message = "Thanks for playing"

def ask_to_repeat():
    engine.say(repeat_message)
    engine.runAndWait()
    repeat = input(f"{repeat_message}? (y/n) ")
    if repeat.lower() == 'y':
        main()
    else:
        print(f"{bye_message}!")
        engine.say(bye_message)
        engine.runAndWait()

def main():
    a = random.randint(1, 100)
    guess_count = 1
    
    print(f"\n|| {greetings} ||")
    engine.say(greetings)
    engine.runAndWait()

    while True: 
        n = int(input("Make your guess: "))
        if (a > n):
            engine.say(higher)
            engine.runAndWait()
            print(f"{higher}: ")
            guess_count += 1 
        elif (a < n):
            engine.say(lower)
            engine.runAndWait()
            print(f"{lower}: ")
            guess_count += 1
        else:
            win_message = f"Bingo! You have guessed it right in {guess_count} tries!"
            print(f"{win_message}")
            engine.say(win_message)
            engine.runAndWait()
            ask_to_repeat()
            break
   
if __name__ == "__main__":
    main()