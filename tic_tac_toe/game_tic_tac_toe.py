import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение размеров окна и клеток
WINDOW_SIZE = 300
CELL_SIZE = WINDOW_SIZE // 3
LINE_WIDTH = 15

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Создание окна
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Крестики-нолики')

# Инициализация игрового поля
board = [['' for _ in range(3)] for _ in range(3)]


# Функция для рисования сетки, рисуем вертикальную и горизонтальную линию
def draw_grid():
   screen.fill(WHITE)
   for i in range(1, 3):
       pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE), LINE_WIDTH)
       pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WINDOW_SIZE, i * CELL_SIZE), LINE_WIDTH)


# Функция для рисования крестиков и ноликов
def draw_xo():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                pygame.draw.line(screen, RED, (col * CELL_SIZE + 20, row * CELL_SIZE + 20),
                        ((col + 1) * CELL_SIZE - 20, (row + 1) * CELL_SIZE - 20), LINE_WIDTH)
                pygame.draw.line(screen, RED, ((col + 1) * CELL_SIZE - 20, row * CELL_SIZE + 20),
                                 (col * CELL_SIZE + 20, (row + 1) * CELL_SIZE - 20), LINE_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, RED, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2),
                                   CELL_SIZE // 2 - 20, LINE_WIDTH)


# Функция для проверки победителя
def check_winner():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '':
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[0][0]:
        return board[0][2]

    return None


# Основной игровой цикл
current_player = 'X'
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] // CELL_SIZE
            mouseY = event.pos[1] // CELL_SIZE
            if board[mouseY][mouseX] == '':
                board[mouseY][mouseX] = current_player
                if check_winner() is None:
                    current_player = 'O' if current_player == 'X' else 'X'
                else:
                    game_over = True

    draw_grid()
    draw_xo()
    pygame.display.update()

    if game_over:
        winner = check_winner()
        font = pygame.font.Font(None, 74)
        text = font.render(f'{winner} wins!', True, RED)
        screen.blit(text, (WINDOW_SIZE // 2 - text.get_width() // 2, WINDOW_SIZE // 2 - text.get_height() // 2))
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

