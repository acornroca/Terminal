import pygame

pygame.init()

#sets initial screen
screen_x = 500
screen_y = 425
screen = pygame.display.set_mode((screen_x, screen_y))

pygame.display.set_caption("readme.txt")

screen_col_a = 255
screen_col_b = 255
screen_col_c = 255

title_font = pygame.font.SysFont("Segoe Script", 21, True)
title_surface = title_font.render("Welcome to Terminal!!", True, (0,0,0))
text_font = pygame.font.SysFont("Segoe UI", 15)
text_surface = text_font.render("Terminal is a visual text-based adventure made entirely in pygame." \
                                "\nThis is a personal project made only with passion, blood, and tears." \
                                "\n\nThe parser works by taking the first word as a keyword." \
                                "\nLike: go, talk, open." \
                                "\nAnd then takes the rest of the message as what to do." \
                                "\nEX: open readme.txt, tells the program to open the file readme.txt" \
                                "\nIf the phrase you entered does not do anything, the program will you tell so." \
                                "\n\n- - First, try the keyword *go* with, I dunno a color? wink wink. - -" \
                                "\n\nI hope you enjoy!", True, (0,0,0))
signature_font = pygame.font.SysFont("Simsun", 60, True, True)
signature_surface = signature_font.render("Acorn", True, (255,190,190))

#clock
clock = pygame.time.Clock()

x = 0

#gameloop
running = True
while running:

    pygame.display.set_caption(str(x))

    x += 1

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

    title_rect = title_surface.get_rect(center=(screen.get_width()//2, 50))
    screen.blit(title_surface, title_rect)

    text_rect = text_surface.get_rect(center=(screen.get_width()//2, 200))
    screen.blit(text_surface, text_rect)

    signature_rect = signature_surface.get_rect(center=(screen.get_width()//2, 370))
    screen.blit(signature_surface, signature_rect)

    #renders all changes to window
    pygame.display.flip()

    delta_time = clock.tick(60)