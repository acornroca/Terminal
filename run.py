import subprocess
import sys
import pygame
from floors.uni_files.characters import filidh

pygame.quit()

main_file_path = R"Terminal\floors\main_gameloop.py"
red_file_path = R"Terminal\floors\red_gameloop.py"

subprocess.run([sys.executable, main_file_path])

if filidh.bools[6]:
    filidh.bools[6] = False
    print("test")
    subprocess.run([sys.executable, red_file_path])