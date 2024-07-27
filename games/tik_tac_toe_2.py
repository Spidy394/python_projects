import random

def replace(n, x, o):
    return 'X' if x[n] else ('O' if o[n] else str(n))

def display_board(x, o):
    print(f"\n{replace(0, x, o)} | {replace(1, x, o)} | {replace(2, x, o)}")
    print("--|---|---")
    print(f"{replace(3, x, o)} | {replace(4, x, o)} | {replace(5, x, o)}")
    print("--|---|---")
    print(f"{replace(6, x, o)} | {replace(7, x, o)} | {replace(8, x, o)}\n")

def check_win(x, o):
    wins = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}]
    for win in wins:
        if all(x[i] for i in win):
            print("X won the game")
            return 1
        if all(o[i] for i in win):
            print("O won the game.")
            return 0
    return -1

def main():
    choies_rem = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    x_state = [0] * 9
    o_state = [0] * 9
    turn = 1 # 1 for X, 0 for O
    print("\n|| Welcome to Tic-Tac-Toe ||")
    while True:
        display_board(x_state, o_state)
        if turn == 1:
            value = int(input("X turn: "))
            if 0 <= value <= 8 and x_state[value] == 0 and o_state[value] == 0:
                x_state[value] = 1
                choies_rem.remove(value)
            else:
                print("Invalid input, please try again.")
                continue
        else:
            value = random.choice(choies_rem)
            print(f"O turn: {value}")
            o_state[value] = 1
            choies_rem.remove(value)

        if check_win(x_state, o_state) != -1:
            break

        turn = 1 - turn

if __name__ == "__main__":
    main()