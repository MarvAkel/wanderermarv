from tkinter import *
from Hero import Hero
import os

d = os.getcwd()
map_array = []
for filename in os.listdir(d):
    if filename.endswith(".txt"):
        with open(filename, 'r') as f:
            for line in f.readlines():
                map_array.append(line)

IMG_SIZE = 72
def draw_map():
    single_coords = [0, 0]
    wall_coords = []
    end = 0
    for lines in range(len(map_array)):
        start = 0
        for block in range(10):
            current_string = map_array[lines][block]
            if current_string == "F":
                start += IMG_SIZE
            elif current_string == "X":
                start += IMG_SIZE
                single_coords[0] = block
                single_coords[1] = lines
                wall_coords.append(tuple(single_coords))
        end += IMG_SIZE

    return wall_coords

wall = draw_map()
print(wall)