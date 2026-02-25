import pygame
import red_functions
from uni_files.keyboard import keyboard_inputs
from uni_files.talk_speed import talk_speed
from uni_files.characters import filidh

pygame.init()

#sets initial screen
screen_x = 0
screen_y = 0
screen = pygame.display.set_mode((screen_y, screen_y))

pygame.display.set_caption("TERMINAL_FM09193110002")

#color of bg
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

    #print(sum(all_talking))
    #print(keyboard_enable)

    #clock
    clock.tick(60)
    start_time = pygame.time.get_ticks()

    #event checker
    for event in pygame.event.get():

        #if user closes window
        if event.type == pygame.QUIT:
            with open(R"Terminal\floors\uni_files\level_checker.txt", 'w') as file:
               file.write("2")
            running = False

        #if user clicks any button
        if event.type == pygame.KEYDOWN:
            if keyboard_enable:
                current += keyboard_inputs(event.key)

            #if user clicks backspace
            if event.key == pygame.K_BACKSPACE:
                if not current[len(current)-1] == '>':
                    current = current[0:len(current)-1]

            #if user clicks enter
            if keyboard_enable:
                if event.key == pygame.K_RETURN:

                    #sends message that user typed to submit() in functions.py and saves to two variables
                    #affect is what it changes, value is how much it changes or what it changes to
                    try:
                        value, affect = red_functions.submit(current.replace(" ",""))
                    except:
                        value, affect = "",""

                    #print(value)

                    #whenever Filidh types
                    if affect == "dialogue_Filidh":
                        keyboard_enable = False
                        pygame.time.set_timer(filidh.events[0],4000)
                        filidh.temps[0] = ""
                        filidh.temps[1] = value
                        pygame.time.set_timer(filidh.events[1],5)

                    #quits program
                    if affect == "quit":
                        with open(R"Terminal\floors\uni_files\level_checker.txt", 'w') as file:
                            file.write("2")
                        running = False

                    #resets message after entering
                    current = '>'
                    
        if event.type == filidh.events[1]:
            next_char = talk_speed(filidh.temps[1], filidh.temps[2])
            if next_char == "stop":
                keyboard_enable = True
                filidh.temps[1] = ''
                filidh.temps[2] = 0
                pygame.time.set_timer(filidh.events[1],0)
            else:
                if filidh.temps[1][filidh.temps[2]] == '#':
                    filidh.temps[0] += "\n"
                elif filidh.temps[1][filidh.temps[2]] == '$':
                    filidh.temps[0] = ''
                else:
                    filidh.temps[0] += next_char
                filidh.temps[2] += 1
                pygame.time.set_timer(filidh.events[1],2)

        #decides when the text disappears from screen
        if event.type == filidh.events[0]:
            filidh.temps[0] = ""
            
    #paints over frame
    screen.fill((screen_col_a,screen_col_b,screen_col_c))

    #text for user typing
    typing_surface = typing_font.render(current, True, (255-screen_col_a,255-screen_col_b,255-screen_col_c))
    typing_rect = typing_surface.get_rect(center=(screen.get_width()//2,screen.get_height()-50))
    if keyboard_enable:
        screen.blit(typing_surface, typing_rect)

    #text for filidh typing
    filidh.text_surface = filidh.text_font.render(filidh.temps[0], True, (255-screen_col_a,255-screen_col_b,255-screen_col_c))
    filidh.text_rect = filidh.text_surface.get_rect(center=(screen.get_width()//2, 50))
    screen.blit(filidh.text_surface, filidh.text_rect)

    #renders all changes to window
    pygame.display.flip()

    delta_time = clock.tick(60)

pygame.quit()