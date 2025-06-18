import pygame

class Projectile:
    def __init__(self, color, x, y, x_vel, y_vel, size):
        self.color = color
        self.x = x
        self.y = y
        self.y_vel = y_vel
        self.x_vel = x_vel
        self.size = size
        self.gravity = 0.5
        self.deadProjectile = False   

    def move(self):
        self.x += self.x_vel
        self.y_vel-=self.gravity
        self.y -= self.y_vel


    def update(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y),self.size)
        self.move()