import pygame

pygame.init()

screen_x = 0
screen_y = 0
screen = pygame.display.set_mode((screen_y, screen_y))

items = []

class Character:
    def __init__(self,name,dialogue,images,events,custom_events,bools,temps,text_font,text_surface,text_rect):
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

class Fighter:
    def __init__(self,name,dialogue,images,events,custom_events,bools,temps,text_font,text_surface,text_rect,
                 HP, focus, moves, items):
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
        self.HP = HP
        self.focus = focus
        self.moves = moves
        self.items = items
    
    def change_HP(self, value):
        self.HP = value

    def change_focus(self, value):
        self.focus = value

    def info_move(self, move_name):
        split = self.moves[move_name].split("/")
        damage = split[0]
        focus = split[1]
        desc = split[2]
        return "DMG: " + damage + " Focus cost: " + focus + " | " + desc
    
    def narrate_move(self, move_name):
        return self.moves[move_name].split("/")[3]

    def info_item(self, item_name):
        return self.items[item_name].split("/")[0]
    
    def narrate_item(self, item_name):
        return self.items[item_name].split("/")[1]

# Regular Characters : Castor, Filidh
# Fighter Characters : Ted
# If a NPC is both Regular and Fighter, it will end with a _r or _f for each respective type

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
castor_care1 = True
castor_care2 = False
castor_care3 = False

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
castor_bools = [castor_appear, castor_blinking, castor_sleeping, castor_care1, castor_care2, castor_care3]
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

#filidh's lists
filidh_events = [filidh_text_disappear, filidh_text_speed, filidh_change_timer]
filidh_custom_events = [filidh_text_disappear_custom, filidh_text_speed_custom, filidh_change_timer_custom]
filidh_bools = [filidh_appear, red_door_appear, red_key_have, filidh_repeat, filidh_repeat_activate, filidh_change_main, filidh_change_red] #remember to save for other colors
filidh_temps = [filidh_text, filidh_text_temp, filidh_text_chr, filidh_repeat_counter]

#- - - - - - - - TED - - - - - - - -#

#ted's bools
ted_appear = False
ted_turn_switch1 = False
ted_turn_switch2 = True
ted_turn = False
ted_brace = False

#ted's text

#ted's dialogue

#ted's turn timer
ted_turn_trigger = pygame.event.custom_type()
ted_turn_trigger_custom = pygame.event.Event(ted_turn_trigger)
ted_fight_anim = pygame.event.custom_type()
ted_fight_anim_custom = pygame.event.Event(ted_fight_anim)

#ted's moves
ted_slump_desc = "10/-10/No other effects./Ted slumps against you, causing you to stagger back a little."
ted_brace_desc = "0/-20/Ted takes 50%% less damage next attack./ Ted braces for impact."

#ted's items
ted_cotton_desc = "Recovers 20 of Ted's HP and focus/Ted stuffed his face with the cotton."

#ted's lists
ted_bools = [ted_appear, ted_turn_switch1, ted_turn_switch2, ted_turn, ted_brace]
ted_events = [ted_turn_trigger, ted_fight_anim]
ted_custom_events = [ted_turn_trigger_custom, ted_fight_anim_custom]
ted_moves = {"slump":ted_slump_desc, "brace":ted_brace_desc}
ted_items = {"cotton":ted_cotton_desc}

#- - - - - - - - INVENI_f - - - - - - - -#

#inveni's bools

#inveni's fight animation
inv_fight_anim = pygame.event.custom_type()
inv_fight_anim_custom = pygame.event.Event(inv_fight_anim)
#image

#inveni's moves
inv_slash_desc = "20/-10/No other effects./You slash with your sword."
inv_cleave_desc = "50/-50/No other effects./You cleave downwards with your sword, marking your enemy."
inv_deflect_desc = "0/20/You take 50%% less damage next attack./You ready your sword, waiting for your enemy's attack."
inv_poise_desc = "0/-20/Your next attack does 20 more damage./You centered yourself, and poise yourself for your next attack."

#inveni's items
inv_potion_desc = "Recovers 20 of your HP./You drink your potion, down to the last drop."

#inveni's lists
inv_events = [inv_fight_anim]
inv_custom_events = [inv_fight_anim_custom]
inv_moves = {"slash":inv_slash_desc, "cleave":inv_cleave_desc, "deflect":inv_deflect_desc, "poise":inv_poise_desc}
inv_items = {"potion":inv_potion_desc}

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
                   castor_text_rect)

filidh = Character("Filidh", 
                   filidh_dialogue, 
                   "", 
                   filidh_events, 
                   filidh_custom_events, 
                   filidh_bools, 
                   filidh_temps, 
                   filidh_text_font, 
                   filidh_text_surface,
                   filidh_text_rect)

ted = Fighter("Ted", 
              "", 
              "", 
              ted_events, 
              ted_custom_events, 
              ted_bools, 
              "", 
              "", 
              "", 
              "", 
              100, 
              100, 
              ted_moves, 
              ted_items)

inveni = Fighter("Inveni",
                 "",
                 "",
                 inv_events,
                 inv_custom_events,
                 "",
                 "",
                 "",
                 "",
                 "",
                 100,
                 100,
                 inv_moves,
                 inv_items)

#list of all Characters
all_characters = [castor,filidh]

#list of all Characters appeared
all_appeared = [filidh.bools[0],castor.bools[0]]