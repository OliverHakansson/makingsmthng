import pygame

class Projectile:
    def __init__(self, color, x, y, y_vel, x_vel, size):
        self.color = color
        self.x = x
        self.y = y
        self.y_vel = y_vel
        self.x_vel = x_vel
        self.size = 15
        self.gravity = 0.5

    def move(self):
        self.x += self.x_vel
        self.y_vel+=self.gravity
        self.y -= self.y_vel

    def update(self, screen):
        self.move()
        pygame.draw.circle(screen, self.color, self.size, (self.x, self.y))