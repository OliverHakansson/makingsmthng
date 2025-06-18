import pygame
import random

class Balloon:
    def __init__(self, size, x, y, targetY, targetX, xSpeed, ySpeed, verticalOscillationZone, horizontalOscillationZone):
        self.size = size
        self.x =  x
        self.y = y
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.bouyancyForce = 0.25
        self.targetY = targetY
        self.targetX = targetX
        self.dampener = 25
        self.verticalOscillationZone = verticalOscillationZone
        self.horizontalOscillationZone = horizontalOscillationZone
    
    def move(self):
        if abs(self.targetY - self.y) < 1:
            self.targetY = random.randint(self.verticalOscillationZone[0],self.verticalOscillationZone[1])
        self.ySpeed = (self.targetY-self.y)/self.dampener  #TODO - change 10 to be an actual value that means something
        self.y += self.ySpeed

        if abs(self.targetX - self.x) < 1:
            self.targetX = random.randint(self.horizontalOscillationZone[0],self.horizontalOscillationZone[1])
        self.xSpeed = (self.targetX-self.x)/self.dampener #TODO - change 10 to be an actual value that means something
        self.x += self.xSpeed

    def collision(self, projectiles, player):
        for i in range(len(projectiles)):
            dx = self.x - projectiles[i].x
            dy = self.y - projectiles[i].y
            distance = (dx ** 2 + dy ** 2) ** 0.5
            if distance < self.size + projectiles[i].size:
                projectiles[i].deadProjectile = True
                i-=1
                player.points+=1

    def draw(self, screen):
        for i in range (self.size, 0, -15):
            if (self.size - i)/15 % 2 == 0:
                pygame.draw.circle(screen, (255,0,0), (self.x, self.y), i)
            else:
                pygame.draw.circle(screen, (255,255,255), ( self.x,self.y), i)

    def update(self, screen):
        self.move()
        self.draw(screen)
        


        