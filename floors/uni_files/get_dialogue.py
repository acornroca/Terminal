from uni_files.characters import all_characters, items

#input: npc talking and phrase that the user typed out 
#processing: search in the files of the text file, find the line with the same phrase as what the user typed,
#            divide the parts up, makes sure the right booleans are True and False, switches the booleans that are listed,
#            and finally return what the npc will say
#output: what the npc will say
def get_dialogue(npc, phrase):
    phrase = phrase.replace(" ","").replace('>','')
    dialogue_lines = npc.dialogue.split("\n")

    if phrase == "items":
        list_of_items = ""
        num = False
        for x in items:
            list_of_items += x
            if num:
                list_of_items += ", " + x
            num = True
        return "ITEMS: " + list_of_items

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
            for chr in all_characters:
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
                        for chr in all_characters:
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