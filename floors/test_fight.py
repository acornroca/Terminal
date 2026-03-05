import pygame
from uni_files.keyboard import keyboard_inputs

pygame.init()

#sets initial screen
screen_x = 0
screen_y = 0
screen = pygame.display.set_mode((screen_x, screen_y))

pygame.display.set_caption("test_fight")

square = pygame.image.load(R"Terminal\floors\red_floor\red_images\test_square.png").convert_alpha()
square = pygame.transform.scale(square, (100,100))

screen_col_a = 255
screen_col_b = 255
screen_col_c = 255

#text for typing
typing_font = pygame.font.SysFont("Arial", 25)
current = ">"
typing_surface = typing_font.render(current, True, (0,0,0))
keyboard_enable = True

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

        #if user clicks any button
        if event.type == pygame.KEYDOWN:
            if keyboard_enable:
                current += keyboard_inputs(event.key)

            #if user clicks backspace
            if event.key == pygame.K_BACKSPACE:
                if not current[len(current)-1] == '>':
                    current = current[0:len(current)-1]

    #paints over frame
    screen.fill((screen_col_a,screen_col_b,screen_col_c))

    screen.blit(square, (screen.get_width()//2-50, screen.get_height()//2-150))

    #text for user typing
    typing_surface = typing_font.render(current, True, (255-screen_col_a,255-screen_col_b,255-screen_col_c))
    typing_rect = typing_surface.get_rect(center=(screen.get_width()//2,screen.get_height()-50))
    if keyboard_enable:
        screen.blit(typing_surface, typing_rect)

    #renders all changes to window
    pygame.display.flip()

    delta_time = clock.tick(60)