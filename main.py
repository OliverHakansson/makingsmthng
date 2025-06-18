import pygame
from player import Player
from projectile import Projectile
from balloon import Balloon

pygame.init()

screen = pygame.display.set_mode((1280, 720))

clock = pygame.time.Clock()

player1 = Player(200, 600, (200, 0, 0), {"throw":pygame.K_w}, False)
player2 = Player(1100, 600, (0, 0, 200), {"throw":pygame.K_UP}, True)

balloonatic = Balloon(75, 300, 300, 300, 300, 0, 0, [220,500], [480,800])
gameState = "gameOver"
while True:
    if gameState=="playing":
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
        if player1.points > 9    or player2.points > 9:
            gameState = "gameOver"
    
    if gameState == "gameOver":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameState="playing"
                    player1.points = 0
                    player2.points = 0
                    break
        screen.fill((0,50,100))
        font = pygame.font.SysFont(None, 100)
        if player2.points > player1.points:
            message = "Blue has Won!"
        elif player2.points < player1.points:
            message = "Red has Won!"
        else:
            message = "A Perfect Tie!"
        screen.blit(font.render(f"{message}", True, (255,255,0)), (400,180))
        font = pygame.font.SysFont(None, 50)
        screen.blit(font.render("Press space to play", True, (255,255,255)), (475,500))

        
    

    pygame.display.flip()
    clock.tick(60)