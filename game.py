import pygame
import pickle
import pygame_gui
from board import GameBoard
from tile import Tile
import colors




class App:
    def __init__(self):
        pygame.init()
        self.width = 1080
        self.height = 720
        self.font = pygame.font.Font(None,24)
        self.paintInstructionSurface = self.font.render("Left Click: PAINT",
                                                        True,
                                                        colors.BLACK)
        self.eraseInstructionSurface = self.font.render("Right Click: ERASE",
                                                        True,
                                                        colors.BLACK)
        self.colorInstructionSurface = self.font.render("Press 'C' to change color", 
                                                        True, 
                                                        colors.BLACK)
        self.blockInstructionSurface = self.font.render("Press 'B' to set blocks",
                                                        True,
                                                        colors.BLACK)
        self.playerInstructionSurface = self.font.render("Press 'P' to set the player(initial Pos)",
                                                         True,
                                                         colors.BLACK)
        
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill((220, 220, 220))
        self.screen.blit(self.paintInstructionSurface,(100,50))
        self.screen.blit(self.eraseInstructionSurface,(100,100))
        self.screen.blit(self.colorInstructionSurface,(100,150))
        self.screen.blit(self.blockInstructionSurface,(100,200))
        self.screen.blit(self.playerInstructionSurface,(400,125))
        self.colorIndex = 0
        self.colorSelector = colors.BLACK
        self.board = GameBoard(screen=self.screen)
        self.matrix = self.board.board_to_matrix()
        self.load_Coords()
        self.runState = True
        self.paintState = False
        self.eraseState = False
        self.playerState = False
        self.blockState = False
        
        
    
    def run(self):
        while self.runState:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runState = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    if event.button == 1:
                        self.paintState = True
                        self.paintClick(x,y)
                    elif event.button == 3:
                        self.eraseState = True
                        self.eraseClick(x,y)
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
                        print("\n\n\n\n\n",self.matrix)
                    elif event.key == pygame.K_DOWN:
                        self.save_Coords()
                        print("Coords saved")
                    elif event.key == pygame.K_UP:
                        self.load_Coords()
                        print("Coords Loaded")
                    elif event.key == pygame.K_c:
                        self.changeColor()
                    elif event.key == pygame.K_b:
                        self.blockState = True
                        self.playerState = False
                    elif event.key == pygame.K_p:
                        self.blockState = False
                        self.playerState = True    

            self.board.draw_board(screen=self.screen)
            # number of x tiles = 83
            # number of y tiles = 35

            pygame.display.update()
        
    def paintClick(self, x, y):
        tile_x = x // (self.board.tile_size + self.board.margin)
        tile_y = (y - self.board.grid[0][0].y) // (self.board.tile_size + self.board.margin)

        if 0 <= tile_x < self.board.grid_width and 0 <= tile_y < self.board.grid_height:
            tile = self.board.grid[tile_x][tile_y]
            tile.color = self.colorSelector
            if self.blockState:
                tile.playerFlags = False
                tile.blockFlags = True    
            elif self.playerState:
                tile.playerFlags = True
                tile.blockFlags = False
            self.matrix = self.board.board_to_matrix()
    
    def eraseClick(self, x, y):
        tile_x = x // (self.board.tile_size + self.board.margin)
        tile_y = (y - self.board.grid[0][0].y) // (self.board.tile_size + self.board.margin)

        if 0 <= tile_x < self.board.grid_width and 0 <= tile_y < self.board.grid_height:
            tile = self.board.grid[tile_x][tile_y]
            tile.color = (255, 255, 255)
            tile.playerFlags = False
            tile.blockFlags = False
            self.matrix = self.board.board_to_matrix()
    
    def save_Coords(self):
        colored_tiles = []
        for i in range(len(self.board.grid)):
            for j in range(len(self.board.grid[i])):
                tile = self.board.grid[i][j]
                blockFlag = tile.blockFlags
                playerFlag = tile.playerFlags
                color = tile.color
                if self.board.grid[i][j].blockFlags or self.board.grid[i][j].playerFlags:
                    colored_tiles.append((i, j, blockFlag, playerFlag, color))

        print(colored_tiles)  # Add this line to check the content of colored_tiles

        with open('ColoredTiles_Cords.pkl', 'wb') as f:
            pickle.dump(colored_tiles, f)
    
    def load_Coords(self):
    # Load the colored_tiles list from the pickle file
        with open('ColoredTiles_Cords.pkl', 'rb') as file:
            colored_tiles = pickle.load(file)
        print(colored_tiles)
        for tile_data in colored_tiles:
            print(tile_data)
            x, y = tile_data[0], tile_data[1]
            blockFlag = tile_data[2]
            playerFlag = tile_data[3]
            color = tile_data[4]
            tile = Tile(
                (x * (self.board.tile_size + self.board.margin)) + self.board.margin,
                ((y * (self.board.tile_size + self.board.margin)) + self.board.margin) + 235,
                self.board.tile_size,
                self.board.tile_size,
                color,  # Color
                blockFlag,
                playerFlag
            )
            self.board.grid[x][y] = tile
            if tile.blockFlags:
                self.matrix[x][y] = 'X'
            elif tile.playerFlags:
                self.matrix[x][y] = 'P'
                        
    
    def changeColor(self):
        colorList = [colors.BLACK, 
                 colors.WHITE, 
                 colors.BLUE, 
                 colors.RED, 
                 colors.GREEN, 
                 colors.GREY]
        if self.colorIndex + 1 == len(colorList):
            self.colorIndex = 0
        else:
            self.colorIndex = self.colorIndex + 1
        self.colorSelector = colorList[self.colorIndex]
         
    
        
            

        
        
