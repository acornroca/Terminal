import pygame
import uni_files.characters as characters
from uni_files.get_dialogue import get_dialogue

pygame.init()

def submit(phrase):
    phrase = phrase.replace('>','')

    #phrases that quit program
    if phrase == "quit" or phrase == "67" or phrase == "kys":
        return "", "quit"

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

#REMEMBER TO ADD A BOOL FOR IN FIGHT OR NOT ###############################################
def submit_fight(phrase, enemies):
    phrase = phrase.replace('>','')

    #phrases that quit program
    if phrase == "quit" or phrase == "67" or phrase == "kys":
        return "", "quit"
    
    if phrase[0:6] == "attack":
        try:
            rest_of_phrase = phrase[6:].split("with")
            enemy_attacked = rest_of_phrase[0]
            attack = rest_of_phrase[1]
            if enemy_attacked in enemies:
                if attack in characters.inveni.moves.keys():
                    return attack, "attack"
        except:
            pass


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