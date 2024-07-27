def replace(n, x, z):
    return 'X' if x[n] else ('O' if z[n] else str(n))

def print_board(x, z):
    print(f"\n{replace(0, x, z)} | {replace(1, x, z)} | {replace(2, x, z)}")
    print("--|---|---")
    print(f"{replace(3, x, z)} | {replace(4, x, z)} | {replace(5, x, z)}")
    print("--|---|---")
    print(f"{replace(6, x, z)} | {replace(7, x, z)} | {replace(8, x, z)}\n")

def win_check(x, z):
    wins = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}]
    for win in wins:
        if all(x[i] for i in win):
            print("X won the game")
            return 1
        if all(z[i] for i in win):
            print("O won the game.")
            return 0
    return -1

def main():
    x_state = [0] * 9
    z_state = [0] * 9
    turn = 1  # 1 -> X and 0 -> O
    print("\n|| Welcome to Tic-Tac-Toe ||")
    while True:
        print_board(x_state, z_state)
        if turn == 1:
            value = int(input("X turn: "))
            if 0 <= value <= 8 and x_state[value] == 0 and z_state[value] == 0:
                x_state[value] = 1
            else:
                print("Invalid input, please try again.")
                continue
        else:
            value = int(input("O turn: "))
            if 0 <= value <= 8 and x_state[value] == 0 and z_state[value] == 0:
                z_state[value] = 1
            else:
                print("Invalid input, please try again.")
                continue
        
        if win_check(x_state, z_state) != -1:
            break
        
        turn = 1 - turn

if __name__ == "__main__":
    main()
