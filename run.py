import subprocess
import sys
import pygame

level_checker_txt = R"Terminal\floors\uni_files\level_checker.txt"
main_file_path = R"Terminal\floors\main_gameloop.py"
red_file_path = R"Terminal\floors\red_gameloop.py"

switch = False
main = False
red = False

level_change = [main,red]

running = True
while running:

    level_num = 0
    with open(level_checker_txt, 'r') as file:
        lines = file.read()
        for line in lines.split("\n"):
            if line == "1":
                print("enabled")
                switch = True
                level_change[level_num] = True
                break
            level_num += 1

    if switch:
        with open(level_checker_txt, 'w') as file:
            file.write("0\n0")
        switch = False

        if level_change[0]:
            subprocess.run([sys.executable, main_file_path])
            level_change[0] = False

        if level_change[1]:
            subprocess.run([sys.executable, red_file_path])
            level_change[1] = False