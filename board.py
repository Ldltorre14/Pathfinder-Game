import pygame
from tile import Tile
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class GameBoard:
    def __init__(self, screen):
        self.screenWidth, self.screenHeight = screen.get_size()
        self.tile_size = 10
        self.margin = 3  # Margin between tiles
        self.grid_width = self.screenWidth // (self.tile_size + self.margin) 
        self.grid_height = (self.screenHeight // (self.tile_size + self.margin)) - 20 
        self.grid = [[Tile((x * (self.tile_size + self.margin)) + self.margin, ((y * (self.tile_size + self.margin)) + self.margin) + 235 , self.tile_size, self.tile_size, (255,255,255), False) for y in range(self.grid_height)] for x in range(self.grid_width)]
        
    def draw_board(self, screen):
        for row in self.grid:
            for tile in row:
                tile.draw(screen)
    
    def board_to_matrix(self):
        matrix = [[' ' for _ in range(self.grid_height)] for _ in range(self.grid_width)]
        for i in range(self.grid_width):
            for j in range(self.grid_height):
                if self.grid[i][j].flags:
                    matrix[i][j] = 'X'
        return matrix
    




