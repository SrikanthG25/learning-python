import pygame
from pygame.locals import *

pygame.init()

WINDOW_SIZE = (640, 640)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Chess Game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)

SQUARE_SIZE = 80
BOARD_SIZE = SQUARE_SIZE * 8
MARGIN = (WINDOW_SIZE[0] - BOARD_SIZE) // 2

PAWN = pygame.image.load("pawn.png")
ROOK = pygame.image.load("rook.png")
KNIGHT = pygame.image.load("knight.png")
BISHOP = pygame.image.load("bishop.png")
QUEEN = pygame.image.load("queen.png")
KING = pygame.image.load("king.png")

board = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
         ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
         [' ', '.', ' ', '.', ' ', '.', ' ', '.'],
         ['.', ' ', '.', ' ', '.', ' ', '.', ' '],
         [' ', '.', ' ', '.', ' ', '.', ' ', '.'],
         ['.', ' ', '.', ' ', '.', ' ', '.', ' '],
         ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
         ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]

game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_running = False

    screen.fill(LIGHT_GRAY)
    for row in range(8):
        for col in range(8):
            x = MARGIN + col * SQUARE_SIZE
            y = MARGIN + row * SQUARE_SIZE
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, WHITE, (x, y, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen, DARK_GRAY, (x, y, SQUARE_SIZE, SQUARE_SIZE))

            if board[row][col] == 'P':
                screen.blit(PAWN, (x, y))
            elif board[row][col] == 'R':
                screen.blit(ROOK, (x, y))
            elif board[row][col] == 'N':
                screen.blit(KNIGHT, (x, y))
            elif board[row][col] == 'B':
                screen.blit(BISHOP, (x, y))
            elif board[row][col] == 'Q':
                screen.blit(QUEEN, (x, y))
            elif board[row][col] == 'K':
                screen.blit(KING, (x, y))
            elif board[row][col] == 'p':
                screen.blit(PAWN, (x, y))
            elif board[row][col] == 'r':
                screen.blit(ROOK, (x, y))
            elif board[row][col] == 'n':
                screen.blit(KNIGHT, (x, y))
            elif board[row][col] == 'b':
                screen.blit