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
keys = pygame.key.get_pressed()
game_active = False


### player
player = pygame.image.load("graphics/shooting.png").convert_alpha()
player = pygame.transform.rotozoom(player, 0, 0.25)
player_rect = player.get_rect(midbottom = (100, 368))

### background
background = pygame.image.load("graphics/night sky.jfif").convert_alpha()
font_surface = font.render("Score: ", False, "Red")
font_rect = font_surface.get_rect(center = (350, 50))
start_surface = font.render("Shoot all the asteroids before they hit you", False, "Orange")
start_rect = start_surface.get_rect(center = (360, 350))
title_surface = font.render("ASTEROID DESTROYER", False, "Orange")
title_rect = title_surface.get_rect(center = (350, 50))
title_asteroid = pygame.image.load("graphics/asteroid_title.png").convert_alpha()
title_asteroid = pygame.transform.rotozoom(title_asteroid, 340, 0.25)
title_asteroid_rect = title_asteroid.get_rect(center = (600, 150))
title_asteroid_rect_2 = title_asteroid.get_rect(center = (500, 100))
title_player_rect = player.get_rect(midbottom = (100, 320))
play_surface = font.render("Place space to play", False, "Orange")
play_surface = pygame.transform.rotozoom(play_surface, 0, 0.8)
play_rect = play_surface.get_rect(center = (360, 320))



### asteroid 
asteroid = pygame.image.load("graphics/asteroid.png").convert_alpha()
asteroid = pygame.transform.rotozoom(asteroid, 0, 0.25)
asteroid_rect = asteroid.get_rect(center = (600, 100))
asteroid_2 = pygame.image.load("graphics/asteroid.png").convert_alpha()
asteroid_2 = pygame.transform.rotozoom(asteroid_2, 0, 0.1)
asteroid_rect_2 = asteroid.get_rect(center = (600, 300))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
        if game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True


            ### collisions
            mouse_pos = pygame.mouse.get_pos()
            if asteroid_rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONUP:
                counter += 1
                asteroid_rect.x = 900
            elif asteroid_rect_2.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONUP:
                counter += 1
                asteroid_rect_2.x = 900
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                asteroid_rect.x = 900
                asteroid_rect_2.x = 900
                counter = 0
                game_active = True



    if game_active:
        screen.blit(background, (0,0))
        screen.blit(player, player_rect)
 
        score = display_score()

        asteroid_rect.x -= 5
        if asteroid_rect.x <= 0:
            game_active = False
        screen.blit(asteroid, asteroid_rect)

        asteroid_rect_2.x -= 4
        if asteroid_rect_2.x <= 0:
            game_active = False
        screen.blit(asteroid_2, asteroid_rect_2)


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