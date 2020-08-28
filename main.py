import pygame
import sys

pygame.init()
width, height = 600, 600

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku Solver")

FPS = 30

clock = pygame.time.Clock()

game_status = True
dis = pygame.font.Font('Font/Roboto-Black.ttf', 30)

board_ = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def getEmptySpot(b_copy):
    for i in range(len(b_copy)):
        for j in range(len(b_copy[0])):
            if b_copy[i][j] == 0:
                return i, j

    return None


def for_place_digit():
    for i in range(len(board_)):
        empty = getEmptySpot(board_)

        if not empty:
            return True
        else:
            row, col = empty

        for j in range(1, 10):
            if check_for_valid_move(j, row, col):
                board_[row][col] = j
                pygame.display.update()

                if for_place_digit():
                    return True

                board_[row][col] = 0
                pygame.display.update()

        return False


def check_for_valid_move(num, r, c):
    # check for row
    for i in range(len(board_[0])):
        if board_[r][i] == num and c != i:
            return False

    # check for column
    for i in range(len(board_[0])):
        if board_[i][c] == num and r != i:
            return False

    box_x = c // 3
    box_y = r // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board_[i][j] == num and (i, j) != (r, c):
                return False

    return True


def draw_grid():
    g = width // 9

    x = 0
    y = 0
    count = 0
    for i in range(width):
        x += g
        y += g
        if count == 2 or count == 5:
            pygame.draw.line(display, [255, 255, 255], (x, 0), (x, height), 4)
            pygame.draw.line(display, [255, 255, 255], (0, y), (width, y), 4)
        else:
            pygame.draw.line(display, [255, 255, 255], (x, 0), (x, height))
            pygame.draw.line(display, [255, 255, 255], (0, y), (width, y))

        count += 1


def board_to_gui():
    g = width // 9

    sx = 0
    sy = 0
    ex = g
    ey = g
    for i in range(9):
        for j in range(9):
            if board_[i][j] is not 0:
                font = dis.render(str(board_[i][j]), True, (255, 255, 255))
                display.blit(font, ((((sx + ex) // 2) - 10), (((sy + ey) // 2) - 14)))
            sx += g
            ex += g
        sx = 0
        ex = g
        sy += g
        ey += g


while game_status:
    display.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_status = False
            sys.exit()

    draw_grid()
    board_to_gui()
    for_place_digit()
    pygame.display.update()
