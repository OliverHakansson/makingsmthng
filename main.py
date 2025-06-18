import pygame
from player import Player
from projectile import Projectile
from balloon import Balloon

pygame.init()

screen = pygame.display.set_mode((1280, 720))

clock = pygame.time.Clock()

player1 = Player(200, 600, (200, 0, 0), {"throw":pygame.K_e})
player2 = Player(1100, 600, (0, 0, 200), {"throw":pygame.K_SLASH})

balloonatic = Balloon(30, 300, 300, 300, 300, 0, 0, [100, 200], [100, 200])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    for event in pygame.event.get():
            if event.type == player1.keys["throw"]:
                player1.throw(screen, Projectile)

    for event in pygame.event.get():
            if event.type == player2.keys["throw"]:
                player2.throw(screen, Projectile)
        
    
    screen.fill((0, 50, 100))
    player1.update(screen, Projectile)
    player2.update(screen, Projectile)
    balloonatic.update(screen)
    

    pygame.display.flip()
    clock.tick(60)