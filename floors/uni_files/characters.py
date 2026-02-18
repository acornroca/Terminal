import pygame

pygame.init()

screen_x = 0
screen_y = 0
screen = pygame.display.set_mode((screen_y, screen_y))

class Player:
    def __init__(self,bools):
        self.items = []
        self.bools = bools

    def add_item(self, item):
        self.items.add(item)

player_bools = []

player = Player(player_bools)

class Character:
    def __init__(self,name,dialogue,images,events,custom_events,bools,temps,text_font,text_surface,text_rect,changer):
        self.name = name
        self.dialogue = dialogue
        self.images = images
        self.events = events
        self.custom_events = custom_events
        self.bools = bools
        self.temps = temps
        self.text_font = text_font
        self.text_surface = text_surface
        self.text_rect = text_rect
        self.changer = changer #only filidh

#- - - - - - - - CASTOR - - - - - - - -#

#castor's images and timing for animations
castor_idle = pygame.image.load(R"Terminal\floors\main_floor\main_images\Castor_idle.png").convert_alpha()
castor_idle2 = pygame.image.load(R"Terminal\floors\main_floor\main_images\Castor_idle2.png").convert_alpha()
castor_blink = pygame.event.custom_type()
castor_blink_custom = pygame.event.Event(castor_blink)

#castor bools
castor_appear = False
castor_blinking = False
castor_sleeping = True

#castor's text
castor_text = "zzz"
castor_text_temp = ""
castor_text_font = pygame.font.SysFont("indieflower", 35)
castor_text_surface = castor_text_font.render(castor_text, True, (0,0,0))
castor_text_rect = castor_text_surface.get_rect(center=(screen.get_width()//2 + 200, screen.get_height()//4+200))
castor_text_speed = pygame.event.custom_type()
castor_text_speed_custom = pygame.event.Event(castor_text_speed)
castor_text_chr = 0

#castor's dialogue
castor_dialogue_filepath = R"Terminal\floors\main_floor\main_dialogues\castor_dialogue.txt"
castor_dialogue_open = open(castor_dialogue_filepath)
castor_dialogue = castor_dialogue_open.read()
castor_dialogue_open.close()

#castor's lists
castor_images = [castor_idle, castor_idle2]
castor_events = [castor_blink, castor_text_speed]
castor_custom_events = [castor_blink_custom, castor_text_speed_custom]
castor_bools = [castor_appear, castor_blinking, castor_sleeping]
castor_temps = [castor_text, castor_text_temp, castor_text_chr]

#- - - - - - - - FILIDH - - - - - - - -#

#filidh bools
filidh_appear = True
red_door_appear = False
red_key_have = True
filidh_repeat = False
filidh_repeat_activate = False
filidh_change_main = False
filidh_change_red = False
filidh_change_timer = pygame.event.custom_type()
filidh_change_timer_custom = pygame.event.Event(filidh_change_timer)

#filidh's text
filidh_text = ""
filidh_text_temp = ""
filidh_text_font = pygame.font.Font(R"Terminal\floors\uni_files\Terminal.ttf", 25)
filidh_text_surface = filidh_text_font.render(filidh_text, True, (0,0,0))
filidh_text_rect = filidh_text_surface.get_rect(center=(screen.get_width()//2 + 200, screen.get_height()//4+200))
filidh_text_disappear = pygame.event.custom_type()
filidh_text_disappear_custom = pygame.event.Event(filidh_text_disappear)
filidh_text_speed = pygame.event.custom_type()
filidh_text_speed_custom = pygame.event.Event(filidh_text_speed)
filidh_text_chr = 0
filidh_repeat_counter = 0

#filidh's dialogue
filidh_dialogue_filepath = R"Terminal\floors\uni_files\filidh_dialogue.txt"
filidh_dialogue_open = open(filidh_dialogue_filepath)
filidh_dialogue = filidh_dialogue_open.read()
filidh_dialogue_open.close()

#changer
c_main = False
c_red = False

#filidh's lists
filidh_events = [filidh_text_disappear, filidh_text_speed, filidh_change_timer]
filidh_custom_events = [filidh_text_disappear_custom, filidh_text_speed_custom, filidh_change_timer_custom]
filidh_bools = [filidh_appear, red_door_appear, red_key_have, filidh_repeat, filidh_repeat_activate, filidh_change_main, filidh_change_red] #remember to save for other colors
filidh_temps = [filidh_text, filidh_text_temp, filidh_text_chr, filidh_repeat_counter]
filidh_changer = [c_main,c_red]

#characters
#name,dialogue,images,appear,text_font,text_surface
castor = Character("Castor", 
                   castor_dialogue, 
                   castor_images, 
                   castor_events, 
                   castor_custom_events, 
                   castor_bools, 
                   castor_temps, 
                   castor_text_font, 
                   castor_text_surface,
                   castor_text_rect,
                   "")

filidh = Character("Filidh", 
                   filidh_dialogue, 
                   "", 
                   filidh_events, 
                   filidh_custom_events, 
                   filidh_bools, 
                   filidh_temps, 
                   filidh_text_font, 
                   filidh_text_surface,
                   filidh_text_rect,
                   filidh_changer)

#list of all Characters
all_characters = [castor,filidh]

#list of all Characters appeared
all_appeared = [filidh.bools[0],castor.bools[0]]