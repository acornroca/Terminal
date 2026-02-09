import pygame
import functions 
from characters import castor, filidh, all_characters

#sets initial screen
screen_x = 0
screen_y = 0
screen = pygame.display.set_mode((screen_y, screen_y))

#color of bg
screen_col_a = 255
screen_col_b = 255
screen_col_c = 255

#text for typing
typing_font = pygame.font.SysFont("Arial", 25)
current = ">"
typing_surface = typing_font.render(current, True, (0,0,0))
keyboard_enable = True

#door image
door = pygame.image.load(R"Terminal\main_floor\door.png").convert_alpha()

#clock
clock = pygame.time.Clock()

#for font in pygame.font.get_fonts():
#    print(font)

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
            running = False

        #if user clicks any button
        if event.type == pygame.KEYDOWN:
            if keyboard_enable:
                current += functions.keyboard_inputs(event.key)

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
                        value, affect = functions.submit(current.replace(" ",""))
                    except:
                        value, affect = "",""

                    #print(value)

                    #changes bg color, value is rgb
                    if affect == "screen_color":
                        value = value.split(",")
                        screen_col_a = int(value[0])
                        screen_col_b = int(value[1])
                        screen_col_c = int(value[2])
                        castor.bools[0] = False
                        filidh.bools[0] = True

                    #interact with castor, value is what he says, what he is doing, etc.
                    if affect == "guide":
                        if value == "meeting":
                            screen_col_a = 158
                            screen_col_b = 193
                            screen_col_c = 245
                            castor.bools[0] = True
                            #filidh.bools[0] = False
                            pygame.time.set_timer(castor.events[0],3500)

                    #interact with castor, and talk with him
                    if affect == "dialogue_Castor":
                        keyboard_enable = False
                        print("disabled false c")
                        castor.temps[0] = ""
                        castor.temps[1] = value
                        pygame.time.set_timer(castor.events[1],20)

                    #whenever Filidh types
                    if affect == "dialogue_Filidh":
                        keyboard_enable = False
                        print("disabled false f")
                        pygame.time.set_timer(filidh.events[0],4000)
                        filidh.temps[0] = ""
                        filidh.temps[1] = value
                        pygame.time.set_timer(filidh.events[1],5)

                    #quits program
                    if affect == "quit":
                        running = False

                    #this whole chunk is if you make f1 say the talk tutorial 3 times
                    #if the repeat counter == 2, add one to repeat counter, turn off repeat, and turn on repeat_activate
                    if filidh.temps[3] == 2 and castor.bools[0]:
                        filidh.temps[3] += 1
                        filidh.bools[3] = False
                        filidh.bools[4] = True
                    #if the repeat counter == 3 ie after you make f3 angry, turn off appear so they stop talking
                    elif filidh.temps[3] == 3 and castor.bools[0]:
                        filidh.bools[0] = False
                    #if repeat is True, add one to the repeat counter and disable repeat so that it can be renabled by the dialogue
                    #if repeat is False, add one to the repeat counter and that is it.
                    elif filidh.bools[3] and castor.bools[0]:
                        filidh.temps[3] += 1
                        filidh.bools[3] = False

                    #resets message after entering
                    current = '>'

        #timers for castor blinking
        #when castor appears, starts a timer. when the timer ends, castor starts blinking, which starts the timer again.
        #when the timer ends, castor stops blinking and starts the timer again to eventually start blinking. looping
        if event.type == castor.events[0]: #250, 3500
            if not castor.bools[1]:                              #castor_blinking
                castor.bools[1] = True                           #castor_blinking
                pygame.time.set_timer(castor.events[0],250)
            elif castor.bools[1]:                                #castor_blinking
                castor.bools[1] = False                          #castor_blinking
                pygame.time.set_timer(castor.events[0],3500)

        #timers for castor's text so that it scrolls instead of appearing all at once
        #starts a timer, and everytime it ends, add a character to the string so that it is displayed.
        #when it recieves stop, it stops getting new characters.
        #if it sees #, it goes to the next line.
        #if it sees $, it goes to the next page.
        if event.type == castor.events[1]:
            next_char = functions.talk_speed(castor.temps[1], castor.temps[2])
            if next_char == "stop":
                keyboard_enable = True
                castor.temps[1] = ''
                castor.temps[2] = 0
                pygame.time.set_timer(castor.events[1],0)
            else:
                if castor.temps[1][castor.temps[2]] == '#':
                    castor.temps[0] += "\n"
                elif castor.temps[1][castor.temps[2]] == '$':
                    castor.temps[0] = ''
                else:
                    castor.temps[0] += next_char
                castor.temps[2] += 1
                pygame.time.set_timer(castor.events[1],20)
        
        if event.type == filidh.events[1]:
            next_char = functions.talk_speed(filidh.temps[1], filidh.temps[2])
            if next_char == "stop":
                keyboard_enable = True
                print(next_char)
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
                pygame.time.set_timer(filidh.events[1],5)

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

    #text for castor talking
    castor.text_rect = castor.text_surface.get_rect(center=(screen.get_width()//2 + 200, screen.get_height()//4+200))
    castor.text_rect.x = screen.get_width()//2 + 150
    castor.text_surface = castor.text_font.render(castor.temps[0], True, (0,0,0))

    #decides what frame of castor is being printed depending on if he is blinking or not
    if castor.bools[0]:
        screen.blit(castor.text_surface, castor.text_rect)
        if not castor.bools[1]:
            screen.blit(castor.images[0], (screen.get_width()//4, screen.get_height()//4))
        elif castor.bools[1]:
            screen.blit(castor.images[1], (screen.get_width()//4, screen.get_height()//4))

    #doors
    if screen_col_a == 255 and screen_col_b == 0 and screen_col_c == 0:
        screen.blit(door, (screen.get_width()//4 + 100, screen.get_height()//6))
        filidh.bools[1] = True

    #renders all changes to window
    pygame.display.flip()

    delta_time = clock.tick(60)

pygame.quit()