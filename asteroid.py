from circleshape import *
from constants import *
from logger import *
import random
import pygame


class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x ,y ,radius)
        

    def draw(self,screen):
        pygame.draw.circle(screen, "white",self.position,self.radius,LINE_WIDTH )
    
    def update(self,dt):
        self.position = self.position + (self.velocity * dt)

    def Split(self):
        if megaduplication == True:
            pass
            if self.radius <= ASTEROID_MIN_RADIUS:
                return
            else:
                log_event("asteroid_split")
                angle = random.uniform(20,50)
                value1 = self.velocity.rotate(angle)
                value2 = self.velocity.rotate(angle)

                newvalue = self.radius - ASTEROID_MIN_RADIUS
                roid1 = Asteroid(self.position.x, self.position.y, self.radius)
                roid2 = Asteroid(self.position.x, self.position.y, self.radius)
                
                roid1.velocity = value1 * 1.2
                roid2.velocity = value2 * 1.2
        else:
            if self.radius <= ASTEROID_MIN_RADIUS:
                pygame.sprite.Sprite.kill(self)
                return
            else:
                pygame.sprite.Sprite.kill(self)
                log_event("asteroid_split")
                angle = random.uniform(20,50)
                value1 = self.velocity.rotate(angle)
                value2 = self.velocity.rotate(angle)

                newvalue = self.radius - ASTEROID_MIN_RADIUS
                roid1 = Asteroid(self.position.x, self.position.y, newvalue)
                roid2 = Asteroid(self.position.x, self.position.y, newvalue)
                
                roid1.velocity = value1 * 1.2
                roid2.velocity = value2 * 1.2

