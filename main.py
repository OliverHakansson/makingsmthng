import pygame
from player import Player
from projectile import Projectile
from balloon import Balloon

pygame.init()

screen = pygame.display.set_mode((1280, 720))

clock = pygame.time.Clock()

player1 = Player(200, 600, (200, 0, 0), {"throw":pygame.K_SPACE}, False)
player2 = Player(1100, 600, (0, 0, 200), {"throw":pygame.K_SLASH}, True)

balloonatic = Balloon(75, 300, 300, 300, 300, 0, 0, [220,500], [480,800]) #100,200, and 100,200

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == player1.keys["throw"]:
                player1.throw()
            if event.key == player2.keys["throw"]:
                player2.throw()


    screen.fill((0, 50, 100))
    pygame.draw.circle(screen,(255,255,255),(625,0),55)
    player1.update(screen)

    player2.update(screen)
    balloonatic.collision(player1.projectiles, player1)
    balloonatic.collision(player2.projectiles, player2)
    balloonatic.update(screen)
    

    pygame.display.flip()
    clock.tick(60)