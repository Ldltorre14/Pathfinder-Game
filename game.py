import pygame
import pickle
import pygame_gui
from board import GameBoard
from tile import Tile

class App:
    def __init__(self):
        pygame.init()
        self.width = 1080
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill((220, 220, 220))
        self.board = GameBoard(screen=self.screen)
        self.matrix = self.board.board_to_matrix()
        self.runState = True
        self.paintState = False
        self.eraseState = False
        
    
    def run(self):
        while self.runState:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runState = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.paintState = True
                    elif event.button == 3:
                        self.eraseState = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.paintState = False
                    elif event.button == 3:
                        self.eraseState = False
                elif event.type == pygame.MOUSEMOTION:
                    x,y = pygame.mouse.get_pos()
                    if self.paintState:
                        self.paintClick(x,y)
                    elif self.eraseState:
                        self.eraseClick(x,y)    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        print(self.matrix)
                    elif event.key == pygame.K_DOWN:
                        self.save_Coords()
                        print("Coords saved")
                    elif event.key == pygame.K_UP:
                        self.load_Coords()
                        print("Coords Loaded")

            self.board.draw_board(screen=self.screen)
            # number of x tiles = 83
            # number of y tiles = 35

            pygame.display.update()
        
    def paintClick(self, x, y):
        tile_x = x // (self.board.tile_size + self.board.margin)
        tile_y = (y - self.board.grid[0][0].y) // (self.board.tile_size + self.board.margin)

        if 0 <= tile_x < self.board.grid_width and 0 <= tile_y < self.board.grid_height:
            tile = self.board.grid[tile_x][tile_y]
            tile.color = (0, 0, 255)
            tile.flags = True
            self.matrix = self.board.board_to_matrix()
    
    def eraseClick(self, x, y):
        tile_x = x // (self.board.tile_size + self.board.margin)
        tile_y = (y - self.board.grid[0][0].y) // (self.board.tile_size + self.board.margin)

        if 0 <= tile_x < self.board.grid_width and 0 <= tile_y < self.board.grid_height:
            tile = self.board.grid[tile_x][tile_y]
            tile.color = (255, 255, 255)
            tile.flags = False
            self.matrix = self.board.board_to_matrix()
    
    def save_Coords(self):
        colored_tiles = []
        for i in range(len(self.board.grid)):
            for j in range(len(self.board.grid[i])):
                if self.board.grid[i][j].flags:
                    colored_tiles.append((i, j))

        with open('ColoredTiles_Cords.pkl', 'wb') as f:
            pickle.dump(colored_tiles, f)
    
    def load_Coords(self):
    # Load the colored_tiles list from the pickle file
        with open('ColoredTiles_Cords.pkl', 'rb') as file:
            colored_tiles = pickle.load(file)

        for coord in colored_tiles:
            x, y = coord
            tile = Tile(
                (x * (self.board.tile_size + self.board.margin)) + self.board.margin,
                ((y * (self.board.tile_size + self.board.margin)) + self.board.margin) + 235,
                self.board.tile_size,
                self.board.tile_size,
                (0, 0, 255),  # Color
                True  # Flags
            )
            self.board.grid[x][y] = tile
            self.matrix[x][y] = 'X'
            


        
        
