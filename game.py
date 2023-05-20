import pygame
import pygame_gui
from board import GameBoard

class App:
    def __init__(self):
        pygame.init()
        self.width = 1080
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill((0,0,0))
        self.board = GameBoard(screen=self.screen)
        self.runState = True
        
    
    def run(self):
        while self.runState:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runState = False
            
            self.board.draw_board(screen=self.screen)
            pygame.display.update()        
        
    
                
            
        
        