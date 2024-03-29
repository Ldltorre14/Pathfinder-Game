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
        self.grid = [[Tile((x * (self.tile_size + self.margin)) + self.margin, ((y * (self.tile_size + self.margin)) + self.margin) + 235 , self.tile_size, self.tile_size, (255,255,255), False,False,False,False) for y in range(self.grid_height)] for x in range(self.grid_width)]
        
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
                elif self.grid[i][j].goalFlags:
                    matrix[i][j] = 'G'
                elif self.grid[i][j].visitedFlags:
                    matrix[i][j] = 'V'
        return matrix
    
    def get_Player_Pos(self):
        for i in range(self.grid_width):
            for j in range(self.grid_height):
                if self.grid[i][j].playerFlags:
                    return i,j
        print("No existent Player in the board")

    def get_Goal_Pos(self):
        for i in range(self.grid_width):
            for j in range(self.grid_height):
                if self.grid[i][j].goalFlags:
                    return i,j
        print("No existent Goal in the board")
    
    def getNeighbours(self,x,y):
        return [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]


