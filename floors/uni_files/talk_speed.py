#input: the phrase typed by user, and what the index of the character that is going to be displayed next
#processing: if there are more characters, return the next character
#output: next character in string
def talk_speed(phrase, chr):
    try:
        if not chr >= len(phrase):
            return phrase[chr]
        else:
            return "stop"
    except:
        return "stop"