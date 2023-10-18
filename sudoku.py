import pygame
import numpy as np
import random

pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("SUDOKU")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Sudoku:
    def __init__(self):
        self.lives = 3
        self.num_list = None
        self.board = None

    def home(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.new_board(2)
            self.home_update()
            pygame.display.flip()
            clock.tick(60)

    def home_update(self):
        win.fill(WHITE)
        title = pygame.image.load("title.png")
        win.blit(title, (400, 0))

    def new_board(self, size):
        self.board = np.empty((size, size, size, size))
        for i in range(size):
            for j in range(size):
                self.num_list = np.array(random.sample(range(1, size**2 + 1), size**2)).reshape((size, size))
                self.board[i, j] = self.num_list
        print(self.board)
        self.check_row(size)
        self.check_col(size)

    def check_row(self, size):
        match = np.zeros((1, 2))
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    if self.board[i, 0, j, k] in self.board[i, 1, j]:
                        match = np.vstack((match, [j, k]))
                        # match = np.array(match)
        if len(match) > 1:
            print(match[0, 0])
            match = np.delete(match, 0, 0)
            for i in range(size):
                for index in range(1, len(match)):
                    if match[0, 0] != match[index, 0]:
                        self.board[i, 0, [int(match[0, 0]), int(match[index, 0])],
                                   [int(match[0, 1]), int(match[index, 1])]] = \
                            self.board[i, 0, [int(match[index, 0]), int(match[0, 0])],
                                       [int(match[index, 1]), int(match[0, 1])]]
                        match = np.delete(match, [0, index], 1)

    def check_col(self, size):
        pass


game = Sudoku()
game.home()
