import sys
import pygame

W = 39

class Cell:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.walls = [True, True, True, True]
        self.visited = False
    

    def show(self, screen):
        x = self.x * W
        y = self.y * W
        if self.walls[0]:
            pygame.draw.line(screen, (0, 255, 0), [x, y], [x+W, y])
        if self.walls[1]:
            pygame.draw.line(screen, (0, 255, 0), [x+W, y], [x+W, y+W])
        if self.walls[2]:
            pygame.draw.line(screen, (0, 255, 0), [x+W, y+W], [x, y+W])
        if self.walls[3]:
            pygame.draw.line(screen, (0, 255, 0), [x, y+W], [x, y])
        if self.visited:
            pygame.draw.rect(screen, (255, 255, 255), (x, y, W, W))
        

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

    def getIndex(self, x, y):
        return x + (y) * self.columns

    def checkNeighbours(self, row, column):
        neighbours = []
        top = self.grid[self.getIndex(row, column - 1)]
        right = self.grid[self.getIndex(row + 1, column)]
        bottom = self.grid[self.getIndex(row, column + 1)]
        left = self.grid[self.getIndex(row - 1, column)]

        if not top.visited:
            neighbours.append(top)
        if not right:
            neighbours.append(right)
        if not bottom.visited:
            neighbours.append(bottom)
        if not left:
            neighbours.append(left)

    def create(self):
        for row in range(self.rows):
            for column in range(self.columns):
                cell = Cell(row, column)
                self.grid.append(cell)

    def draw(self):          
        for cell in range(len(self.grid)):
            self.grid[cell].show(self.screen)
        self.grid[0].visited = True
    
    def run(self):
        self.create()
        while True:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
