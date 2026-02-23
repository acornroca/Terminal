import pygame
import uni_files.characters as characters

pygame.init()

#input: npc talking and phrase that the user typed out 
#processing: search in the files of the text file, find the line with the same phrase as what the user typed,
#            divide the parts up, makes sure the right booleans are True and False, switches the booleans that are listed,
#            and finally return what the npc will say
#output: what the npc will say
def get_dialogue(npc, phrase):
    phrase = phrase.replace(" ","").replace('>','')
    dialogue_lines = npc.dialogue.split("\n")

    for line in dialogue_lines:
        #print("1")
        check1 = False
        check2 = True
        parts = line.split('|')
        accepted_phrases = parts[0].split('/')

        for x in accepted_phrases:
            #print("2")
            if x == '@' or x in phrase:
                #print("check1")
                check1 = True
                break
        for boolean in parts[2].split('/'):
            being_checked = boolean.split('=')[0]
            checks = boolean.split('=')[1]
            #print("3")
            for chr in characters.all_characters:
                if chr.name == being_checked:
                    being_checked = chr

            bool_value = int(checks.split(':')[0])
            T_or_F = checks.split(':')[1]

            if T_or_F == 't':
                if being_checked.bools[bool_value] == False:
                    #print("check2")
                    check2 = False

            elif T_or_F == 'f':
                if being_checked.bools[bool_value] == True:
                    #print("check2")
                    check2 = False

        if check1 and check2:
            try:
                for flip in parts[3].split('/'):
                    if '=' in parts[3]:
                        being_flipped = flip.split('=')[0]
                        flipped = flip.split('=')[1]
                        for chr in characters.all_characters:
                            if chr.name == being_flipped:
                                being_flipped = chr
                    else:
                        flipped = parts[3]

                    #print("4")
                    flip_value = int(flipped.split("->")[0])
                    flip_T_or_F = flipped.split("->")[1]

                    if flip_T_or_F == 't':
                        #print("flipped true")
                        being_flipped.bools[flip_value] = True

                    elif flip_T_or_F == 'f':
                        #print("flipped false")
                        being_flipped.bools[flip_value] = False

            except:
                #print("5")
                pass

            #print(npc.name + " got somethin")
            return parts[1].replace('_',"                    ") #20 spaces

    #print(npc.name + " got nothing")
    return None

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