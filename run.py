import subprocess
import sys
import pygame

#file locations for gameloops and the level checker text
level_checker_txt = R"floors\uni_files\level_checker.txt"
main_file_path = R"Terminal\floors\main_gameloop.py"
red_file_path = R"Terminal\floors\red_gameloop.py"
test_fight_file_path = R"Terminal\floors\test_fight.py"

#bools for what to do
#switch makes sure that the file is only override once
switch = False
quit = False
main = False
red = False
ted = False

#list for all levels
level_change = [main,red,ted]

#gameloop
running = True
while running:

    #what number level is currently being read
    level_num = 0
    with open(level_checker_txt, 'r') as file:
        lines = file.read()
        for line in lines.split("\n"):
            #if the line says "1" that level is opened
            if line == "1":
                print("enabled")
                switch = True
                level_change[level_num] = True
                break
            #if the line says "2" quits the program
            elif line == "2":
                switch = True
                quit = True
            level_num += 1

    #overrides the level checker and opens the right level or quits
    if switch:
        with open(level_checker_txt, 'w') as file:
            file.write("0\n0\n0")
        switch = False

        #quits
        if quit:
            sys.exit()

        #opens main
        if level_change[0]:
            subprocess.run([sys.executable, main_file_path])
            level_change[0] = False

        #opens red
        if level_change[1]:
            subprocess.run([sys.executable, red_file_path])
            level_change[1] = False

        if level_change[2]:
            subprocess.run([sys.executable, test_fight_file_path])