import sys
import pygame
import random

class Maze:
    def __init__(self, height: int, width: int, block_size: int) -> None:
        self.height = height
        self.width = width
        self.block_size = block_size
        self.grid_visited = [[False for _ in range(self.width//self.block_size)] for _ in range(self.height//self.block_size)]
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill((0, 0, 0))

        # Init pygame
        pygame.init()

    def create(self):
        for x in range(0, self.width, self.block_size):
            for y in range(0, self.height, self.block_size):
                rect = pygame.Rect(x, y, self.block_size, self.block_size)
                pygame.draw.rect(self.screen, (255, 255, 255), rect, 1)
        
        for x in range(1, len(self.grid_visited)-1):
            for y in range(1, len(self.grid_visited)-1):
                rect = pygame.Rect(x*self.block_size, y*self.block_size, self.block_size, self.block_size)
                pygame.draw.rect(self.screen, (0, 255, 0), rect, 0)
        
        
    def dfs(self, x, y):
        if self.grid_visited[x][y]:
            return    
        self.grid_visited[x][y] = True
        neighbours = [
            (x-1,y),
            (x, y + 1),
            (x+1, y),
            (x, y-1)
        ]
        for neighbour in neighbours:
            if not self.grid_visited[neighbour[0]][neighbour[1]]:
                rect = pygame.Rect(neighbour[0], neighbour[1], self.block_size, self.block_size)
                pygame.draw.rect(self.screen, (0, 255, 0), rect, 0)
            self.dfs(neighbour[0], neighbour[1])

    def run(self):
        while True:
            self.create()
            # agent = pygame.Rect(y, x, self.block_size, self.block_size)
            # pygame.draw.rect(self.screen, (0, 255, 0), agent, 0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
