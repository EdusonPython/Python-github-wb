from colorama import Fore, Back, Style


def draw_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        print("---------")
        '''print(Fore.RED + 'X' + Style.RESET_ALL)
        print(Fore.BLUE + 'O' + Style.RESET_ALL)
        print(Back.YELLOW + ' ' + Style.RESET_ALL)'''

def ask_and_make_move(player, board):
    x, y = input(f"{player}, enter x and y coordinates (e.g. 0 0): ").strip().split()
    x, y = int(x), int(y)
    if (0<= x <= 2) and (0 <= y <= 2) and (board[x][y] == " "):
        board[x][y] = player
    else:
        print("That spot is already taken, please try again")
        ask_and_make_move(player, board)

def ask_move(player, board):
    x, y = input(f"{player}, enter x and y coordinates (e.g. 0 0): ").strip().split()
    x, y = int(x), int(y)
    if (0<= x <= 2) and (0 <= y <= 2) and (board[x][y] == " "):
        return x, y
    else:
        print("That spot is already taken, please try again")
        return ask_move(player, board)

def make_move(player, board, x, y):
    if board[x][y] != " ":
        print("That spot is already taken, please try again")
        return False
    board[x][y] = player
    return True

def check_win(player, board):
    for i in range(3):
        if board[i] == [player, player, player]:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return True
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True
        return False

def tic_tac_toe():
    while True:
        board = [[" " for i in range(3)] for j in range(3)]
        player = "X"
        while True:
            draw_board(board)
            ask_and_make_move(player, board)
            if check_win(player, board):
                print("Congratulations! You won!")
                break
            tie_game = False
            for row in board:
                for col in row:
                    if col == " ":
                        tie_game = True
            if not tie_game:
                break
            player = "0" if player == "X" else "X"
        restart = input("Do you want to restart? (y/n): ")
        if restart != "y":
            break

tic_tac_toe()