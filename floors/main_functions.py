import pygame
import uni_files.characters as characters
from uni_files.get_dialogue import get_dialogue

pygame.init()

#characters.a.bools[0] = True
#get_dialogue(characters.a, "")
#get_dialogue(characters.a, "")

#input: text that user typed
#processing: finds if text should do anything in program
#output: returns a value and what it should affect
def submit(phrase):
    phrase = phrase.replace('>','')

    #phrases that quit program
    if phrase == "quit" or phrase == "67" or phrase == "kys":
        return "", "quit"

    if phrase[0:2] == 'go':
        phrase = phrase[2:]

        #all phrases that trigger bg changes
        if phrase == "blue":
            return "0,0,255", "screen_color"
        elif phrase == "red" or phrase == "reddoor":
            return "255,0,0", "screen_color"
        elif phrase == "green": 
            return "0,255,0", "screen_color"
        elif phrase == "yellow": 
            return "255,255,0", "screen_color"
        elif phrase == "cyan": 
            return "0,255,255", "screen_color"
        elif phrase == "magenta": 
            return "255,0,255", "screen_color"
        elif phrase == "orange":
            return "255,165,0", "screen_color"
        elif phrase == "purple":
            return "128,0,170", "screen_color"
        elif phrase == "brown":
            return "150,75,0", "screen_color"
        elif phrase == "white":
            return "255,255,255", "screen_color"
        elif phrase == "black":
            return "0,0,0", "screen_color"

        #phrases that trigger rgb changes
        if phrase.replace(",", "").isnumeric():
            phrase = phrase.split(",")
            if int(phrase[0]) >= 0 and int(phrase[0]) <= 255:
                if int(phrase[1]) >= 0 and int(phrase[1]) <= 255:
                    if int(phrase[2]) >= 0 and int(phrase[2]) <= 255:
                        #rgb that triggers castor
                        if int(phrase[0]) == 158 and int(phrase[1]) == 193 and int(phrase[2]) == 245:
                            return "meeting", "guide"
                        return phrase[0] + "," + phrase[1] + "," + phrase[2], "screen_color"

        #phrase that also triggers castor
        if phrase == "castor":
            return "meeting", "guide"
        
        return get_dialogue(characters.filidh, "go"), "dialogue_Filidh"

    #phrase that triggers dialogue of any Character who has appeared
    if phrase[0:4] == "talk":
        for chr in characters.all_characters:
            if chr.bools[0] == True:
                try:
                    talk = get_dialogue(chr,phrase)
                    if talk != None:
                        return talk, "dialogue_" + chr.name
                except:
                    pass
            
    #displays error message if command not found
    if sum(characters.all_appeared) == 1 and characters.all_appeared[0] == True:
        talk = get_dialogue(characters.filidh,phrase)
        if talk != None:
            return talk, "dialogue_Filidh"
        return "AIn-NameError: Command  \"" + phrase + "\" not found", "dialogue_Filidh"
    
    return "",""