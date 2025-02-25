import pygame
from sys import exit

### functions

def display_score():
    global counter
    font_surface = font.render(f"Score: {int(counter)}", False, "Red")
    font_rect = font_surface.get_rect(center = (350, 50))
    screen.blit(font_surface, font_rect)

def collisions(player, asteriod):
    return 0

### global variables
pygame.init()
screen = pygame.display.set_mode((736,368))
clock = pygame.time.Clock()
pygame.display.set_caption("Asteroid destroyer")
font = pygame.font.Font("font/Pixeltype.ttf", 50)
counter = 0
game_active = True


### player
player = pygame.image.load("graphics/shooting.png").convert_alpha()
player = pygame.transform.rotozoom(player, 0, 0.25)
player_rect = player.get_rect(midbottom = (100, 368))

### background
background = pygame.image.load("graphics/night sky.jfif").convert_alpha()
font_surface = font.render("Score: ", False, "Red")
font_rect = font_surface.get_rect(center = (350, 50))
start_surface = font.render("Shoot all the asteroids before they hit you", False, "Green")
start_rect = start_surface.get_rect(center = (360, 350))
title_surface = font.render("ASTEROID DESTROYER", False, "Green")
title_rect = title_surface.get_rect(center = (350, 50))
title_asteroid = pygame.image.load("graphics/asteroid_title.png").convert_alpha()
title_asteroid = pygame.transform.rotozoom(title_asteroid, 340, 0.25)
title_asteroid_rect = title_asteroid.get_rect(center = (600, 150))
title_asteroid_rect_2 = title_asteroid.get_rect(center = (500, 100))
title_player_rect = player.get_rect(midbottom = (100, 320))
play_surface = font.render("Place space to play", False, "Green")
play_surface = pygame.transform.rotozoom(play_surface, 0, 0.8)
play_rect = play_surface.get_rect(center = (360, 310))



### asteroid 
asteroid = pygame.image.load("graphics/asteroid.png").convert_alpha()
asteroid = pygame.transform.rotozoom(asteroid, 0, 0.25)
asteroid_rect = asteroid.get_rect(center = (600, 100))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse down")
    if game_active:
        screen.blit(background, (0,0))
        screen.blit(player, player_rect)
        screen.blit(asteroid, asteroid_rect)
        score = display_score()

        mouse_pos = pygame.mouse.get_pos()
        if player_rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONUP:
            counter += 1
            player_rect.x = 800
            

    else:

        ### start and game over screen
        screen.blit(background, (0,0))
        screen.blit(start_surface, start_rect)
        screen.blit(title_asteroid, title_asteroid_rect_2)
        screen.blit(title_surface, title_rect)
        screen.blit(title_asteroid, title_asteroid_rect)
        screen.blit(player, title_player_rect)
        screen.blit(play_surface, play_rect)
        



    pygame.display.update()
    clock.tick(60)