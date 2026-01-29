from circleshape import CircleShape
from constants import *
from logger import *
import pygame

class shot(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x ,y ,radius)

    def draw(self,screen):
        pygame.draw.circle(screen, "white",self.position,2,LINE_WIDTH )
    
    def update(self,dt):
        self.position = self.position + (self.velocity * dt)