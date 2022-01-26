import sys
import pygame
import random

W = 40

class Cell:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def show(self, screen):
        x = self.x * W
        y = self.y * W
        pygame.draw.line(screen, (0, 255, 0), [x, y], [x+W, y])
        pygame.draw.line(screen, (0, 255, 0), [x+W, y], [x+W, y+W])
        pygame.draw.line(screen, (0, 255, 0), [x+W, y+W], [x, y+W])
        pygame.draw.line(screen, (0, 255, 0), [x, y+W], [x, y])
        

class Maze:
    def __init__(self, height: int, width: int, w: int) -> None:
        self.height = height
        self.width = width
        self.w = w
        self.rows = self.width//w
        self.columns = self.height//w
        self.grid = []

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill((0, 0, 0))

        # Init pygame
        pygame.init()

    def create(self):
        for row in range(self.rows):
            for column in range(self.columns):
                cell = Cell(row, column)
                self.grid.append(cell)

    def draw(self):          
        for cell in range(len(self.grid)):
            self.grid[cell].show(self.screen)

    def run(self):
        self.create()
        while True:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
