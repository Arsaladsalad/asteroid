import pygame
from sys import exit



### global variables
pygame.init()
screen = pygame.display.set_mode((736,368))
clock = pygame.time.Clock()
font = pygame.font.Font("font/Pixeltype.ttf", 50)


### player
player = pygame.image.load("graphics/shooting.png").convert_alpha()
player = pygame.transform.rotozoom(player, 0, 0.25)
player_rect = player.get_rect(midbottom = (100, 368))

### background
background = pygame.image.load("graphics/night sky.jfif").convert_alpha()
font_surface = font.render("Score: ", False, "Red")
font_rect = font_surface.get_rect(center = (350, 50))


### asteroid 
asteroid = pygame.image.load("graphics/asteroid.png").convert_alpha()
asteroid = pygame.transform.rotozoom(asteroid, 0, 0.25)
asteroid_rect = asteroid.get_rect(center = (600, 100))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0,0))
    screen.blit(player, player_rect)
    screen.blit(asteroid, asteroid_rect)
    screen.blit(font_surface, font_rect)

    pygame.display.update()
    clock.tick(60)