import pygame
import projectile
import time
import math

class Player:
    def __init__(self, x, y, color, keys, inverted):
        self.color = color
        self.rect = pygame.Rect(x, y, 50, 50)
        self.projectiles = []
        self.keys=keys
        self.points = 0
        self.x_p = 50
        self.y_p = 50
        self.inverted = inverted
        self.m = 0.005
        self.power = 40
        self.points = 0
        self.timeOfLastShot = time.time()-3
        self.lineColor = (255,255,255)

    def throw(self):

        if time.time()>=self.timeOfLastShot+1.5:
            x_throw = self.power*(self.x_p/100)
            y_throw = self.power*(self.y_p/100)

            if self.inverted==True:
                x_throw *= -1

            p = projectile.Projectile(self.lineColor, self.rect.x+25, self.rect.y+25, x_throw, y_throw, 20)
            self.projectiles.append(p)
            self.timeOfLastShot = time.time()

        

    def aim(self):
        self.x_p+=self.m
        self.y_p = 100-self.x_p
        if self.x_p <= 0 or self.x_p >= 100:
            self.m*=-1

    def update(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

        if self.inverted:
            self.lineColor = (153,50,204)
        else:
            self.lineColor = (255,69,0)
        
        angle = self.x_p*0.9
        lineX = abs(math.cos(angle)*75)
        lineY = abs(math.sin(angle)*75)*-1
        if self.inverted:
            lineX *=-1
        pygame.draw.line(screen, self.lineColor, (self.rect.x+25, self.rect.y+25), (self.rect.x+lineX+25, self.rect.y+lineY+25), 5)

        self.aim()

        for p in self.projectiles:
            p.update(screen)
            if p.deadProjectile == True:
                self.projectiles.remove(p)
        font = pygame.font.SysFont(None, 36)
        text = font.render(f"{self.points}", True, self.lineColor)
        if not self.inverted:
            screen.blit(text, (600,10))
        else:
            screen.blit(text, (640,10))