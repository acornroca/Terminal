import pygame

#input: key being pressed by user
#processing: figures out which key was pressed
#output: returns coresponding letter
def keyboard_inputs(key):
    if key == pygame.K_q:
        return "q"
    elif key == pygame.K_w:
        return "w"
    elif key == pygame.K_e:
        return "e"
    elif key == pygame.K_r:
        return "r"
    elif key == pygame.K_t:
        return "t"
    elif key == pygame.K_y:
        return "y"
    elif key == pygame.K_u:
        return "u"
    elif key == pygame.K_i:
        return "i"
    elif key == pygame.K_o:
        return "o"
    elif key == pygame.K_p:
        return "p"
    elif key == pygame.K_a:
        return "a"
    elif key == pygame.K_s:
        return "s"
    elif key == pygame.K_d:
        return "d"
    elif key == pygame.K_f:
        return "f"
    elif key == pygame.K_g:
        return "g"
    elif key == pygame.K_h:
        return "h"
    elif key == pygame.K_j:
        return "j"
    elif key == pygame.K_k:
        return "k"
    elif key == pygame.K_l:
        return "l"
    elif key == pygame.K_z:
        return "z"
    elif key == pygame.K_x:
        return "x"
    elif key == pygame.K_c:
        return "c"
    elif key == pygame.K_v:
        return "v"
    elif key == pygame.K_b:
        return "b"
    elif key == pygame.K_n:
        return "n"
    elif key == pygame.K_m:
        return "m"
    elif key == pygame.K_SPACE:
        return " "
    elif key == pygame.K_0:
        return "0"
    elif key == pygame.K_1:
        return "1"
    elif key == pygame.K_2:
        return "2"
    elif key == pygame.K_3:
        return "3"
    elif key == pygame.K_4:
        return "4"
    elif key == pygame.K_5:
        return "5"
    elif key == pygame.K_6:
        return "6"
    elif key == pygame.K_7:
        return "7"
    elif key == pygame.K_8:
        return "8"
    elif key == pygame.K_9:
        return "9"
    elif key == pygame.K_COMMA:
        return ","
    elif key == pygame.K_PERIOD:
        return "."
    return ""