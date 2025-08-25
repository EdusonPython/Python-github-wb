# Корректируем игру крестики нолики
# Рисуем игровое поле, используем библиотеку Colorama

from colorama import Fore, Back, Style


def draw_board(board):
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == " ":
                if y < len(board) - 1:
                    print(Back.YELLOW + board[x][y] + Style.RESET_ALL, "| ", end='')
                else:
                    print(Back.YELLOW + board[x][y] + Style.RESET_ALL, "| ")
            elif board[x][y] == "X":
                if y < len(board) - 1:
                    print(Fore.RED + "X" + Style.RESET_ALL, "| ", end='')
                else:
                    print(Fore.RED + "X" + Style.RESET_ALL, "| ")
            elif board[x][y] == "O":
                if y < len(board) - 1:
                    print(Fore.BLUE + "O" + Style.RESET_ALL, "| ", end='')
                else:
                    print(Fore.BLUE + "O" + Style.RESET_ALL, "| ")
        print("---------")

# Создайте функцию, которая запрашивает ход


def ask_move(player, board):
    while True:
        try:
            x, y = (
                input(f"{player}, Введите x и y координаты (пример 0 0): ").strip().split()
            )
            x, y = int(x), int(y)
            if (0 <= x < len(board)) and (0 <= y < len(board)) and (board[x][y] == " "):
                return x, y
            else:
                print(f"Клетка {x} {y} занята или вне диапазона. Попробуйте еще раз.")
        except ValueError:
            print("Некорректный ввод. Введите два числа, разделенные пробелом.")

# Создайте функцию, которая делает ход


def make_move(player, board, x, y):
    board[x][y] = player

# Создайте функцию, которая объединяет запрос хода и сам ход


def ask_and_make_move(player, board):
    x, y = ask_move(player, board)
    make_move(player, board, x, y)


# Создайте функцию, которая проверяет, не был ли код выигрышным


def check_win(player, board):
    # Проверьте, совпадают ли значения в строках и столбцах
    for i in range(len(board)):
        # Проверьте, совпадают ли значения в строках
        if board[i] == [player, player, player]:
            return True
        # Проверьте, совпадают ли значения в столбцах
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    # Проверьте, совпадают ли значения на диагонали из верхнего левого в нижний правый угол
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    # Проверьте, совпадают ли значения на диагонали из верхнего правого в нижний левый угол
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


# Создайте общую функцию, которая управляет игрой


def start_game(board):
    # Запустите бесконечный цикл игры
    while True:
        # Создайте поле с заданным размером
        board = [[" " for i in range(board)] for j in range(board)]
        player = "X"

        # Запустите бесконечный цикл раунда
        while True:
            # Нарисуйте игровое поле
            draw_board(board)

            # Запросите ход
            ask_and_make_move(player, board)

            # Проверьте выигрыш
            if check_win(player, board):
                print(f"{player} выиграл!")
                break

            # Проверьте ничью
            if all(cell != " " for row in board for cell in row):
                print("Ничья!")
                break

            # Передайте ход другому игроку
            player = "0" if player == "X" else "X"

        # Предложите сыграть еще раз, когда игра закончилась
        restart = input("Хотите сыграть еще раз? (y/n)")
        if restart.lower() != "y":
            break

start_game(3)

# Удачной игры

