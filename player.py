import pygame
from projectile import Projectile

class Player:
    def __init__(self, x, y, color, keys):
        self.color = color
        self.rect = (x, y, 100, 100)
        self.projectiles = []
        self.keys=keys

    def throw(self, Projectile):
        p = Projectile((255, 255, 255), self.x, self.y, 4, 4, 40)
        self.projectiles.append(p)

    def update(self, screen, Projectile):
        pygame.draw.rect(screen, self.color, self.rect)

        for p in self.projectiles:
            p.update()