import sys
import pygame


class Maze:
    def __init__(self, height: int, width: int, block_size: int) -> None:
        self.height = height
        self.width = width
        self.block_size = block_size
        self.grid = [[None for _ in range(self.width)] for _ in range(self.height)]
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill((0, 0, 0))

        # Init pygame
        pygame.init()

    def create(self):
        for x in range(0, self.width, self.block_size):
            for y in range(0, self.height, self.block_size):
                rect = pygame.Rect(x, y, self.block_size, self.block_size)
                pygame.draw.rect(self.screen, (255, 255, 255), rect, 1)

    def run(self):
        while True:
            self.create()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
