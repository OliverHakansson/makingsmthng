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
        self.v = 0.5
        self.power = 40
        self.points = 0
        self.timeOfLastShot = time.time()-3
        self.cooldown = 1
        self.lineColor = (255,255,255)

    def throw(self):
        if time.time()>=self.timeOfLastShot+self.cooldown:
            x_throw = self.power*(self.x_p/100)
            y_throw = self.power*(self.y_p/100)

            if self.inverted==True:
                x_throw *= -1

            p = projectile.Projectile(self.lineColor, self.rect.x+25, self.rect.y+25, x_throw, y_throw, 20)
            self.projectiles.append(p)
            self.timeOfLastShot = time.time()
            self.x_p = 90
      
    def aim(self):
        self.x_p+=self.v
        self.y_p = 100-self.x_p
        if self.x_p <= 0 or self.x_p >= 100:
            self.v*=-1

    def indicateAim(self, screen):
        if self.inverted:
            self.lineColor = (153,50,204)
        else:
            self.lineColor = (255,69,0)

        angle = self.x_p*0.9
        lineX = abs(math.sin(math.radians(angle))*75)
        lineY = abs(math.cos(math.radians(angle))*75)*-1
        if self.inverted:
            lineX *=-1
        pygame.draw.line(screen, self.lineColor, (self.rect.x+25, self.rect.y+25), (self.rect.x+lineX+25, self.rect.y+lineY+25), 5)

    def updateProjectiles(self, screen):
        for p in self.projectiles:
            p.update(screen)
            if p.deadProjectile == True:
                self.projectiles.remove(p)

    def displayPoints(self, screen):
        font = pygame.font.SysFont(None, 36)
        text = font.render(f"{self.points}", True, self.lineColor)
        if not self.inverted:
            screen.blit(text, (600,10))
        else:
            screen.blit(text, (640,10))

    def showCoolDown(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.rect.x-25, self.rect.y+75, 100, 10))
        cooldownBarWidth = 100-(100*((self.timeOfLastShot-time.time())/self.cooldown)*-1)
        # if cooldownBarWidth>100:
        #     cooldownBarWidth = 100
        # cooldownBarWidth = 100-cooldownBarWidth
        pygame.draw.rect(screen, (255, 0, 0), (self.rect.x-25, self.rect.y+75, cooldownBarWidth, 10))

    def update(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        self.aim()
        self.indicateAim(screen)
        self.updateProjectiles(screen)
        self.displayPoints(screen)
        self.showCoolDown(screen)
        
        