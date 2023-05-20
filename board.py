import pygame
from tile import Tile
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


import pygame

class GameBoard:
    def __init__(self, screen):
        self.screenWidth, self.screenHeight = screen.get_size()
        tile_size = 10
        margin = 3  # Margin between tiles
        self.grid_width = self.screenWidth // (tile_size + margin) 
        self.grid_height = (self.screenHeight // (tile_size + margin)) - 20
        
        self.grid = [[Tile((x * (tile_size + margin)) + margin, ((y * (tile_size + margin)) + margin) + 235 , tile_size, tile_size, (0,255,255), False) for y in range(self.grid_height)] for x in range(self.grid_width)]
        
    def draw_board(self, screen):
        for row in self.grid:
            for tile in row:
                tile.draw(screen)