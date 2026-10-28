import pygame, sys

pygame.init()
SIZE = 300
screen = pygame.display.set_mode((SIZE, SIZE + 50))
font = pygame.font.SysFont(None, 90)
small = pygame.font.SysFont(None, 32)

board = [""] * 9
turn = "X"
winner = ""

LINES = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def check():
    for a, b, c in LINES:
        if board[a] != "" and board[a] == board[b] == board[c]:
            return board[a]
    if "" not in board:
        return "Draw"
    return ""

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN and winner == "" and e.pos[1] < SIZE:
            i = (e.pos[1] // 100) * 3 + (e.pos[0] // 100)
            if board[i] == "":
                board[i] = turn
                winner = check()
                turn = "O" if turn == "X" else "X"
        if e.type == pygame.KEYDOWN and e.key == pygame.K_r:
            board, turn, winner = [""] * 9, "X", ""

    screen.fill((30, 30, 30))
    for k in (100, 200):                                   # grid lines
        pygame.draw.line(screen, (200, 200, 200), (k, 0), (k, SIZE), 3)
        pygame.draw.line(screen, (200, 200, 200), (0, k), (SIZE, k), 3)
    for i, mark in enumerate(board):
        if mark:
            color = (0, 200, 0) if mark == "X" else (220, 50, 50)
            img = font.render(mark, True, color)
            screen.blit(img, ((i % 3) * 100 + 30, (i // 3) * 100 + 22))

    if winner == "Draw":
        msg = "Draw! Press R"
    elif winner:
        msg = winner + " wins! Press R"
    else:
        msg = "Turn: " + turn
    screen.blit(small.render(msg, True, (255, 255, 255)), (10, SIZE + 12))

    pygame.display.flip()
