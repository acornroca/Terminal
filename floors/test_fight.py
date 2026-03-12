import pygame
import os

screen_loc_x = 0
screen_loc_y = 0
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{screen_loc_x},{screen_loc_y}'

from red_functions import submit_fight
from uni_files.keyboard import keyboard_inputs
from uni_files.talk_speed import talk_speed
from uni_files.characters import filidh, inveni, ted

display_info = pygame.display.Info()

pygame.init()

#sets initial screen
screen_x = display_info.current_w
screen_y = display_info.current_h
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
typing_when = 0
typing_move_y = 0

#text for turn order
turn_order_font = pygame.font.SysFont("Algerian", 30)
turn_order_text = 3
turn_order_surface = turn_order_font.render(str(turn_order_text), True, (0,0,0))

#text for HP
HP_label_font = pygame.font.SysFont("Arial", 25)
HP_label_text = "HP"
HP_label_surface = HP_label_font.render(HP_label_text, True, (0,0,0))

HP_font = pygame.font.SysFont("Colonna", 50)
HP_text = "100"
HP_surface = HP_font.render(HP_text, True, (0,0,0))

#text for Focus
focus_label_font = pygame.font.SysFont("Arial", 25)
focus_label_text = "Focus"
focus_label_surface = focus_label_font.render(focus_label_text, True, (0,0,0))

focus_font = pygame.font.SysFont("Colonna", 50)
focus_text = "100"
focus_surface = focus_font.render(focus_text, True, (0,0,0))

#text for Moves
moves_label_font = pygame.font.SysFont("Arial", 25)
moves_label_text = "Moves"
moves_label_surface = moves_label_font.render(moves_label_text, True, (0,0,0))

moves_font = pygame.font.SysFont("Colonna", 30)
moves_text = "Slash, Cleave, Deflect, Poise"
moves_surface = moves_font.render(moves_text, True, (0,0,0))

#text for Items
items_label_font = pygame.font.SysFont("Arial", 25)
items_label_text = "Items"
items_label_surface = items_label_font.render(items_label_text, True, (0,0,0))

items_font = pygame.font.SysFont("Colonna", 30)
items_text = "Potion"
items_surface = items_font.render(items_text, True, (0,0,0))

enemies = ["ted"]

turn_order = ["inv", "inv", "inv", "ted"]

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

            #if user clicks enter
            if keyboard_enable:
                if event.key == pygame.K_RETURN:

                    #sends message that user typed to submit() in functions.py and saves to two variables
                    #affect is what it changes, value is how much it changes or what it changes to
                    try:
                        value, affect = submit_fight(current.replace(" ",""), enemies)
                    except:
                        value, affect = "",""

                    #print(value)

                    if affect == "attack":
                        attack_name = value
                        info = inveni.moves[attack_name].split("/")
                        ted.change_HP(ted.HP-int(info[0]))
                        inveni.change_focus(inveni.focus+int(info[1]))
                        value = inveni.narrate_move(attack_name)
                        affect = "dialogue_Filidh"
                        print(ted.HP)
                        print(inveni.focus)

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

    screen.blit(square, (screen.get_width()//2-50, screen.get_height()//2-150))

    #text for user typing
    typing_surface = typing_font.render(current, True, (255-screen_col_a,255-screen_col_b,255-screen_col_c))
    if typing_when == 20 and typing_move_y <= 100:
        if typing_move_y <= 20:
            typing_move_y += 10
        elif typing_move_y <= 60:
            typing_move_y += 5
        elif typing_move_y <= 86:
            typing_move_y += 3
        elif typing_move_y <= 95:
            typing_move_y += 1
        elif typing_move_y <= 99:
            typing_move_y += 0.5
    else:
        typing_when += 1

    typing_rect = typing_surface.get_rect(center=(screen.get_width()//2,screen.get_height()-50-(typing_move_y*0.8)))
    turn_order_rect = turn_order_surface.get_rect(center=(50,-40+typing_move_y))
    HP_label_rect = HP_label_surface.get_rect(center=(screen.get_width()//2-100,screen.get_height()+10-typing_move_y))
    HP_rect = HP_surface.get_rect(center=(screen.get_width()//2-100,screen.get_height()+50-typing_move_y))
    focus_label_rect = focus_label_surface.get_rect(center=(screen.get_width()//2+150,screen.get_height()+10-typing_move_y))
    focus_rect = focus_surface.get_rect(center=(screen.get_width()//2+150,screen.get_height()+50-typing_move_y))
    moves_label_rect = moves_label_surface.get_rect(center=(50,screen.get_height()+10-typing_move_y))
    moves_rect = moves_surface.get_rect(topleft=(50,screen.get_height()+50-typing_move_y))
    items_label_rect = items_label_surface.get_rect(center=(screen.get_width()//2+400,screen.get_height()+10-typing_move_y))
    items_rect = items_surface.get_rect(topleft=(screen.get_width()//2+400,screen.get_height()+50-typing_move_y))

    
    if keyboard_enable:
        screen.blit(typing_surface, typing_rect)
    screen.blit(turn_order_surface, turn_order_rect)
    screen.blit(HP_label_surface, HP_label_rect)
    screen.blit(HP_surface, HP_rect)
    screen.blit(focus_label_surface, focus_label_rect)
    screen.blit(focus_surface, focus_rect)
    screen.blit(moves_label_surface, moves_label_rect)
    screen.blit(moves_surface, moves_rect)
    screen.blit(items_label_surface, items_label_rect)
    screen.blit(items_surface, items_rect)

    #text for filidh typing
    filidh.text_surface = filidh.text_font.render(filidh.temps[0], True, (255-screen_col_a,255-screen_col_b,255-screen_col_c))
    filidh.text_rect = filidh.text_surface.get_rect(center=(screen.get_width()//2, 50))
    screen.blit(filidh.text_surface, filidh.text_rect)

    #renders all changes to window
    pygame.display.flip()

    delta_time = clock.tick(60)