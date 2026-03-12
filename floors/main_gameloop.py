import pygame
import random
import subprocess
import sys
import main_functions
from uni_files.keyboard import keyboard_inputs
from uni_files.talk_speed import talk_speed
from uni_files.characters import castor, filidh, items

#sets initial screen
screen_x = 0
screen_y = 0
screen = pygame.display.set_mode((screen_x, screen_y))

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

#images
door = pygame.image.load(R"Terminal\floors\main_floor\main_images\door.png").convert_alpha()
basic_file = pygame.image.load(R"Terminal\floors\main_floor\main_images\file.png").convert_alpha()
basic_file = pygame.transform.scale(basic_file, (100,110))

#basic display text
help_file_font = pygame.font.Font(R"Terminal\floors\uni_files\Terminal.ttf", 17)
help_file_surface = help_file_font.render("README.txt", True, (0,0,0))

#int to randomize what castor will say when asked how they are doing
castor_care_random = 1

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
                        value, affect = main_functions.submit(current.replace(" ",""))
                    except:
                        value, affect = "",""

                    print(value)

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
                            subprocess.run([sys.executable, R"Terminal\floors\uni_files\open_window.py"])

                    #interact with castor, and talk with him
                    if affect == "dialogue_Castor":
                        keyboard_enable = False
                        castor.temps[0] = ""
                        castor.temps[1] = value
                        pygame.time.set_timer(castor.events[1],20)

                    #whenever Filidh types
                    if affect == "dialogue_Filidh":
                        keyboard_enable = False
                        pygame.time.set_timer(filidh.events[0],4000)
                        filidh.temps[0] = ""
                        filidh.temps[1] = value
                        pygame.time.set_timer(filidh.events[1],5)

                    #opens whatever window is being told to open
                    if affect == "open_window":
                        if value == "readme":
                            if screen_col_a == 255 and screen_col_b == 255 and screen_col_c == 255:
                                subprocess.run([sys.executable, R"Terminal\floors\main_floor\main_open_windows\open_help.py"])

                    #quits program
                    if affect == "quit":
                        with open(R"Terminal\floors\uni_files\level_checker.txt", 'w') as file:
                            file.write("2")
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

        #whenever user goes to red, writes "1" in level checker so that run.py knows to go to red
        if event.type == filidh.events[2]:
            with open (R"Terminal\floors\uni_files\level_checker.txt", 'w') as file:
                file.write("0\n1")
            running = False

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
            next_char = talk_speed(castor.temps[1], castor.temps[2])
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

        #Like castor's but for filidh's text
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
            pygame.time.set_timer(filidh.events[0],0)

        #decides which of castor's line is being shown when asked how he is
        if not castor.bools[0]:
            castor_care_random = random.randint(1,3)
            if castor_care_random == 1:
                castor.bools[3] = True
                castor.bools[4] = False
                castor.bools[5] = False
            if castor_care_random == 2:
                castor.bools[3] = False
                castor.bools[4] = True
                castor.bools[5] = False
            if castor_care_random == 3:
                castor.bools[3] = False
                castor.bools[4] = False
                castor.bools[5] = True

    #items
    if not "red key" in items:
        if filidh.bools[2]:
            items.append("red key")

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
    else:
        filidh.bools[1] = False

    #files
    if screen_col_a == 255 and screen_col_b == 255 and screen_col_c == 255:
        screen.blit(basic_file, (screen.get_width()//4 + 200, screen.get_height()//4+100))
        screen.blit(help_file_surface, (screen.get_width()//4 + 205, screen.get_height()//4+215))

    #if changing to red level
    if filidh.bools[6]:
        filidh.bools[6] = False
        pygame.time.set_timer(filidh.events[2], 2000)

    #renders all changes to window
    pygame.display.flip()

    delta_time = clock.tick(60)

pygame.quit()