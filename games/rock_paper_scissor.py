import random

def choice_name(n):
    if n == 1:
        return 'Rock'

    elif n == 2:
        return 'Paper'

    else:
        return 'Scissor'

print("|| Welcome to the Rock-Paper-Scissor Game ||")


while True:
    print("1. Rock\n2. Paper\n3. Scissor\n")
    
    try:
        user_choice = int(input("Enter your choice: "))

        while 1 > user_choice or user_choice > 3:
            user_choice = int(input("Enter a valid choice please: "))
    except ValueError:
        print("Invalid input! Please enter a number (1, 2, or 3)")
        continue

    comp_choice = random.randint(1,3)
    user_choice_name = choice_name(user_choice)
    comp_choice_name =  choice_name(comp_choice)

    print(f"Player choice: {user_choice_name} \nComputer choice: {comp_choice_name}")

    if user_choice_name == comp_choice_name:
        print("Its a tie!")

    elif (user_choice_name == 'Rock' and comp_choice_name == 'Scissor') or (user_choice_name == 'Scissor' and comp_choice_name == 'Paper') or (user_choice_name == 'Paper' and comp_choice_name == 'Rock'):
        print("Player wins!")

    else:
        print("Computer wins!")
    
    repeat = input("Do you want to play again? (y/n) ")
    if repeat.lower() == 'n':
        print("Thanks for playing!")
        break
