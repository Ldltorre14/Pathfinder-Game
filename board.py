import pygame
from tile import Tile



import pygame

class GameBoard:
    def __init__(self, screen):
        self.screenWidth, self.screenHeight = screen.get_size()
        self.tile_size = 10
        self.margin = 3  # Margin between tiles
        self.grid_width = self.screenWidth // (self.tile_size + self.margin) 
        self.grid_height = (self.screenHeight // (self.tile_size + self.margin)) - 20 
        self.grid = [[Tile((x * (self.tile_size + self.margin)) + self.margin, ((y * (self.tile_size + self.margin)) + self.margin) + 235 , self.tile_size, self.tile_size, (255,255,255), False,False) for y in range(self.grid_height)] for x in range(self.grid_width)]
        
    def draw_board(self, screen):
        for row in self.grid:
            for tile in row:
                tile.draw(screen)
    
    def board_to_matrix(self):
        matrix = [[' ' for _ in range(self.grid_height)] for _ in range(self.grid_width)]
        for i in range(self.grid_width):
            for j in range(self.grid_height):
                if self.grid[i][j].blockFlags:
                    matrix[i][j] = 'X'
                elif self.grid[i][j].playerFlags:
                    matrix[i][j] = 'P'
        return matrix
    




