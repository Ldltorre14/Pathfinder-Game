import pygame

class Tile(pygame.Rect):
    def __init__(self, x, y, width, height, color, blockFlags, playerFlags, goalFlags):
        super().__init__(x, y, width, height)
        self.color = color
        self.blockFlags = blockFlags
        self.playerFlags = playerFlags
        self.goalFlags = goalFlags
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self)
