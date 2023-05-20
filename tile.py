import pygame

class Tile(pygame.Rect):
    def __init__(self,x,y,width,height,color,flags):
        super().__init__(x,y,width,height)
        self.color = color
        self.flags = flags
    
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,self)


