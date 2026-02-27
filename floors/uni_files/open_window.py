import pygame

pygame.init()

#sets initial screen
screen_x = 300
screen_y = 250
screen = pygame.display.set_mode((screen_x, screen_y))

screen_col_a = 255
screen_col_b = 255
screen_col_c = 255

#clock
clock = pygame.time.Clock()

#gameloop
running = True
while running:

    #clock
    clock.tick(60)
    start_time = pygame.time.get_ticks()

    #event checker
    for event in pygame.event.get():

        #if user closes window
        if event.type == pygame.QUIT:
            running = False

    #paints over frame
    screen.fill((screen_col_a,screen_col_b,screen_col_c))

    #renders all changes to window
    pygame.display.flip()

    delta_time = clock.tick(60)