import pygame
import sys  # Allows us to access system commands
import random

pygame.init()  # Initilizes the pygame module

screen = pygame.display.set_mode(
    (1280, 720)
)  # Creates the display surface through which we can pop open a window to see the game. The values inside the parenthesis are the width and height of the screen.
clock = pygame.time.Clock()  # Creates an object to determine the fps of game
pygame.mouse.set_visible(False) # Hides the mouse cursor on screen

wood_bg = pygame.image.load(
    "shooting range assets/Wood_BG.png"
)  # Stores the image, creating a surface
land_bg = pygame.image.load("shooting range assets/Land_BG.png")
water_bg = pygame.image.load("shooting range assets/Water_BG.png")
cloud1 = pygame.image.load("shooting range assets/Cloud1.png")
cloud2 = pygame.image.load("shooting range assets/Cloud2.png")
crosshair = pygame.image.load("shooting range assets/crosshair.png")
crosshair_rect = crosshair.get_rect(center = (640,360))
duck_surface = pygame.image.load("shooting range assets/duck.png")

game_font = pygame.font.Font(None,60)
text_surface = game_font.render("YOU WIN!",True,(255,255,255))
text_rect = text_surface.get_rect(center = (640,360))

land_position_y = 560 # Set the starting y position for land_bg
land_speed = 1 # Set speed of land animation

water_position_y = 640
water_speed = 1.3

duck_list = []

for duck in range(20):
    duck_position_x = random.randrange(50, 1200) # Sets the ducks position to a random x value between the given numbers
    duck_position_y = random.randrange(120,600) # Sets the ducks position to a random y value between the given numbers
    duck_rect = duck_surface.get_rect(center = (duck_position_x, duck_position_y)) # Places the rectangles around the ducks
    duck_list.append(duck_rect) # Adds the rectangles to the list to be used later

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # QUIT is the "x" button at the top right of the window
            pygame.quit()  # Uninitiates pygame and ends it as a module
            sys.exit()  # Closes the program that is running in the background on the system

        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair.get_rect(center = event.pos) # You can also use pygame.mouse.get_pos() instead. These commands just get the location of the mouse. But this line draws a rectangle around the center of the mouse so that we can use collision detection.
        if event.type == pygame.MOUSEBUTTONDOWN:
            for index, duck_rect in enumerate(duck_list): # Iterates through the list, then using enumerate it gives the index of what item I'm looking at in the list allowing us to give the duck an identifier
                if duck_rect.collidepoint(event.pos):
                    del duck_list[index] # Removes the duck from the list, making it disappear from the screen

    screen.blit(
        wood_bg, (0, 0)
    )  # arg1 is the surface we want to place, arg2 is where we want to place it. arg2 represents a coordinate plane so (x,y). Increasing x moves it to the right, increasing y moves it down.
    for duck_rect in duck_list:
        screen.blit(duck_surface, duck_rect) # For each rectangle in duck list a duck is placed on the screen at the same coordinates

    if len(duck_list) <= 0:
        screen.blit(text_surface, text_rect)

    land_position_y -= land_speed
    if land_position_y <= 520 or land_position_y >= 600: # Set boundaries for land animation. So when it goes up a certain amount it will go back down and vice versa.
        land_speed *= -1
    screen.blit(land_bg, (0, land_position_y))

    water_position_y += water_speed

    if water_position_y <= 620 or water_position_y >= 680:
        water_speed *= -1
    screen.blit(water_bg, (0, water_position_y))

    screen.blit(crosshair, crosshair_rect)
    
    screen.blit(cloud1, (50, 30))
    screen.blit(cloud2, (100, 25))

    screen.blit(cloud2, (250, 25))

    screen.blit(cloud1, (450, 35))

    screen.blit(cloud2, (650, 20))

    screen.blit(cloud1, (950, 25))
    screen.blit(cloud2, (1000, 35))

    pygame.display.update()  # This takes anything that came before and draws it on the display surface
    clock.tick(
        120
    )  # Fps is set at 120 fps, it can go slower than this if there are too many elements, but it will never go faster.
