import os
import pdb
import sys
from tkinter import Image
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import random
import numpy as np
import glob

platform_chars_unique = sorted(list(["-","X", "}", "{", "<", ">", "[", "]", "Q", "S"]))
cave_chars_unique = sorted(list(["-","X", "}", "{"]))
cave_doors_chars_unique = sorted(list(["-","X", "}", "{", "b", "B"]))
cave_portals_chars_unique = sorted(list(["-","X", "0", "1", "2", "3"]))
vertical_chars_unique = sorted(list(["-","X", "}", "{"]))
slide_chars_unique = sorted(list(["-","X", "}", "{"]))
sokoban_chars_unique = sorted(list(["-","X", "@", "#", "o"]))

def get_cols_rows_char2int(game):
    if game == "platform":
        int2char = dict(enumerate(platform_chars_unique))
        cols = 16
        rows = 32
    elif game == "cave":
        int2char = dict(enumerate(cave_chars_unique))
        cols = 16
        rows = 32
    elif game == "cave_doors":
        int2char = dict(enumerate(cave_doors_chars_unique))
        cols = 16
        rows = 16
    elif game == "cave_portal":
        int2char = dict(enumerate(cave_portals_chars_unique))
        cols = 16
        rows = 16
    elif game == "vertical":
        int2char = dict(enumerate(vertical_chars_unique))
        cols = 20
        rows = 16
    elif game == "slide":
        int2char = dict(enumerate(slide_chars_unique))
        cols = 32
        rows = 14
    elif game == "sokoban":
        int2char = dict(enumerate(sokoban_chars_unique))
        cols = 16
        rows = 16

    char2int = {ch: ii for ii, ch in int2char.items()}
    return cols, rows, char2int

def load_txt_solvable(game):
    parent_directory_p = f'./{game}/solvable/texts'

    levels = []
    labels = []
    current_block = []
    for _, dirs, _ in os.walk(parent_directory_p):
        for dir in dirs:
            dir_path = os.path.join(parent_directory_p, dir)
            for _, _, files in os.walk(dir_path):
                for file in files:
                    file_path = os.path.join(dir_path, file)
                    with open(file_path, 'r') as file:
                        for line in file:
                            line = line.rstrip('\n')
                            if not line.startswith('META'):
                                levels.append(current_block)
                                current_block = []
                                labels.append(1)

                            elif len(current_block) > 0:
                                current_block.append(line)

    labels = np.array(labels)
    return levels, labels

def load_txt_unsolvable(game):
    parent_directory_p = f'./{game}/unsolvable/texts'

    levels = []
    labels = []
    current_block = []
    for _, dirs, _ in os.walk(parent_directory_p):
        for dir in dirs:
            dir_path = os.path.join(parent_directory_p, dir)
            for _, _, files in os.walk(dir_path):
                for file in files:
                    file_path = os.path.join(dir_path, file)
                    with open(file_path, 'r') as file:
                        for line in file:
                            line = line.rstrip('\n')
                            if not line.startswith('META'):
                                levels.append(current_block)
                                current_block = []
                                labels.append(0)

                            elif len(current_block) > 0:
                                current_block.append(line)
                                        

    labels = np.array(labels)
    return levels, labels

def load_txt(game):
    X1, y1 = load_txt_solvable(game)
    X2, y2 = load_txt_unsolvable(game)

    X = np.concatenate((X1,X2), axis=0)
    y = np.concatenate((y1,y2), axis=0)
    return X, y

def load_img_solvable(game):
    parent_directory_p = f'./{game}/solvable/texts'
    images = []
    labels = []
    for _, dirs, _ in os.walk(parent_directory_p):
        for dir in dirs:
            dir_path = os.path.join(parent_directory_p, dir)
            for _, _, files in os.walk(dir_path):
                for file in files:
                    file_path = os.path.join(dir_path, file)
                    try:
                        with Image.open(file_path) as img:
                            images.append(img.copy())
                            labels.append(1)
                    except Exception as e:
                        print(f"Error opening {file}: {e}")
    return images, labels

def load_img_unsolvable(game):
    parent_directory_p = f'./{game}/unsolvable/texts'
    images = []
    labels = []
    for _, dirs, _ in os.walk(parent_directory_p):
        for dir in dirs:
            dir_path = os.path.join(parent_directory_p, dir)
            for _, _, files in os.walk(dir_path):
                for file in files:
                    file_path = os.path.join(dir_path, file)
                    try:
                        with Image.open(file_path) as img:
                            images.append(img.copy())
                            labels.append(0)
                    except Exception as e:
                        print(f"Error opening {file}: {e}")
    return images, labels

def load_img(game):
    X1, y1 = load_txt_solvable(game)
    X2, y2 = load_txt_unsolvable(game)

    X = np.concatenate((X1,X2), axis=0)
    y = np.concatenate((y1,y2), axis=0)
    return X, y