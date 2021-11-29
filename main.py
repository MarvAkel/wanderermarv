from tkinter import *
import pygame
from Hero import Hero
import os
from skeleton import *
from skeleton2 import *
from skeleton3 import *
from boss import*

STATSIZE = 200
IMG_SIZE = 72
WIDTH = 10 * IMG_SIZE
HEIGHT = 10 * IMG_SIZE + STATSIZE

root = Tk()
root.title('Wanderer Game')
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
skeleton = Skeleton(1, 9, 0, 9)
skeleton2 = Skeleton2(1, 9, 0, 9)
skeleton3 = Skeleton3(1, 9, 0, 9)
hero = Hero()
boss = Boss(1,9,1,9)

d = os.getcwd()
map_array = []

counter = 0
def show_stats():
    canvas.create_text(110, 740,text=f"Hero (Level {hero.lvl}) HP: {hero.hp}/{hero.max_hp} | DP: {hero.dp} | SP: {hero.sp}")


show_stats()


def battle_music():
    file = 'Misty-Bog_remixed.mp3'
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1) # If the loops is -1 then the music will repeat indefinitely.

battle_music()

def battle_stats():
    if hero.x == skeleton.xx and hero.y == skeleton.yy:
        canvas.create_text(122, 760,
                           text=f"Skeleton 1(Level {skeleton.mlvl}) HP: {skeleton.chp}/{skeleton.mhp} | DP: {skeleton.mdp} | SP: {skeleton.msp}")
    elif hero.x == skeleton2.xx and hero.y == skeleton2.yy:
        canvas.create_text(122, 760,
                           text=f"Skeleton 2 (Level {skeleton2.mlvl}) HP: {skeleton2.chp}/{skeleton2.mhp} | DP: {skeleton2.mdp} | SP: {skeleton2.msp}")
    elif hero.x == skeleton3.xx and hero.y == skeleton3.yy:
        canvas.create_text(122, 760,
                           text=f"Skeleton 3 (Level {skeleton3.mlvl}) HP: {skeleton3.chp}/{skeleton3.mhp} | DP: {skeleton3.mdp} | SP: {skeleton3.msp}")
    elif hero.x == boss.xx and hero.y == boss.yy:
        canvas.create_text(122, 760,
                           text=f"Boss (Level {boss.lvl}) HP: {boss.hp}/{boss.mhp} | DP: {boss.dp} | SP: {boss.sp}")




filename = "map1.txt"
with open(filename, 'r') as f:
    for line in f.readlines():
        map_array.append(line)


def draw_map():
    canvas.delete("all")
    single_coords = [0, 0]
    wall_coords = []
    end = 0
    for lines in range(len(map_array)):
        start = 0
        for block in range(10):
            current_string = map_array[lines][block]
            if current_string == "F":
                canvas.create_image(start, end, image=root.floor, anchor=NW)
                start += IMG_SIZE
            elif current_string == "X":
                canvas.create_image(start, end, image=root.wall, anchor=NW)
                start += IMG_SIZE
                single_coords[0] = block
                single_coords[1] = lines
                wall_coords.append(tuple(single_coords))
            elif current_string == "P":
                canvas.create_image(start, end, image=root.portal, anchor=NW)
        end += IMG_SIZE
    canvas.create_image(boss.xx * IMG_SIZE, boss.yy * IMG_SIZE, image=root.boss, anchor=NW)  # boss
    canvas.create_image(skeleton.xx * IMG_SIZE, skeleton.yy * IMG_SIZE, image=root.skeleton, anchor=NW)  # skeleton
    canvas.create_image(skeleton2.xx * IMG_SIZE, skeleton2.yy * IMG_SIZE, image=root.skeleton, anchor=NW)  # skeleton
    canvas.create_image(skeleton3.xx * IMG_SIZE, skeleton3.yy * IMG_SIZE, image=root.skeleton3, anchor=NW)  # skeleton
    canvas.create_image(hero.x * IMG_SIZE, hero.y * IMG_SIZE, image=getattr(root, hero.img), anchor=NW)  # hero
    return wall_coords


# def draw_screen():
#     canvas.create_image(0, 0, image=root.floor, anchor=NW) #Creating a Floor Block
#     canvas.create_image(IMG_SIZE, 0, image=root.wall, anchor=NW) #creating a wall block
#     canvas.create_image(2 * IMG_SIZE, 0, image=root.skeleton, anchor=NW) #skeleton
#     canvas.create_image(3 * IMG_SIZE, 0, image=root.boss, anchor=NW) #boss
#     canvas.create_image(hero.x * IMG_SIZE, hero.y * IMG_SIZE, image=getattr(root, hero.img), anchor=NW) #hero

# Loading images. You can access these loaded images from the root object.
# For example: root.floor or getattr(root, "floor")
def load_images():
    directory = "images/"
    root.floor = PhotoImage(file=directory + "floor.png")
    root.wall = PhotoImage(file=directory + "wall.png")
    root.hero_down = PhotoImage(file=directory + "hero-down.png")
    root.hero_up = PhotoImage(file=directory + "hero-up.png")
    root.hero_right = PhotoImage(file=directory + "hero-right.png")
    root.hero_left = PhotoImage(file=directory + "hero-left.png")
    root.skeleton = PhotoImage(file=directory + "skeleton.png")
    root.skeleton2 = PhotoImage(file=directory + "skeleton.png")
    root.skeleton3 = PhotoImage(file=directory + "skeleton.png")
    root.boss = PhotoImage(file=directory + "boss.png")
    root.strike = PhotoImage(file=directory + "strike.png")
    root.portal = PhotoImage(file=directory + "portal.png")


load_images()

# Binding keyboard key events to functions

wall = draw_map()

def draw_boss():
    boss_position = (boss.xx, boss.yy)
    while boss_position in wall:
        boss.xx = random.randint(0, 9)
        if boss.xx not in wall:
            canvas.create_image(boss.xx * IMG_SIZE, boss.yy * IMG_SIZE, image=root.boss,
                                anchor=NW)  # skeleton
        else:
            pass
    else:
        canvas.create_image(skeleton.xx * IMG_SIZE, skeleton.yy * IMG_SIZE, image=root.skeleton, anchor=NW)  # skeleton


draw_boss()
def draw_skeleton():
    skeleton_position = (skeleton.xx, skeleton.yy)
    while skeleton_position in wall:
        skeleton.xx = random.randint(0, 9)
        if skeleton.xx not in wall:
            canvas.create_image(skeleton.xx * IMG_SIZE, skeleton.yy * IMG_SIZE, image=root.skeleton,
                                anchor=NW)  # skeleton
        else:
            pass
    else:
        canvas.create_image(skeleton.xx * IMG_SIZE, skeleton.yy * IMG_SIZE, image=root.skeleton, anchor=NW)  # skeleton


draw_skeleton()

def draw_skeleton2():
    skeleton_position2 = (skeleton2.xx, skeleton2.yy)
    while skeleton_position2 in wall:
        skeleton2.xx = random.randint(0, 9)
        if skeleton.xx not in wall:
            canvas.create_image(skeleton2.xx * IMG_SIZE, skeleton2.yy * IMG_SIZE, image=root.skeleton2,anchor=NW)  # skeleton
        else:
            pass
    else:
        canvas.create_image(skeleton2.xx * IMG_SIZE, skeleton2.yy * IMG_SIZE, image=root.skeleton2, anchor=NW)  # skeleton

draw_skeleton2()


def draw_skeleton3():

    skeleton_position3 = (skeleton3.xx, skeleton3.yy)
    while skeleton_position3 in wall:
        skeleton3.xx = random.randint(0, 9)
        if skeleton.xx not in wall:
            canvas.create_image(skeleton3.xx * IMG_SIZE, skeleton3.yy * IMG_SIZE, image=root.skeleton3,anchor=NW)  # skeleton
        else:
            pass
    else:
        canvas.create_image(skeleton3.xx * IMG_SIZE, skeleton3.yy * IMG_SIZE, image=root.skeleton3, anchor=NW)


draw_skeleton3()


def spaceBar(event):

    for i in range(400):
        canvas.create_image(hero.x * IMG_SIZE, hero.y * IMG_SIZE, image=getattr(root, "strike"), anchor=NW)
    if hero.x == skeleton.xx and hero.y == skeleton.yy:
        if hero.sp > skeleton.mdp:
            skeleton.striked(hero.sp)
            if skeleton.chp > 0:
                hero.striked(skeleton.msp)
            elif skeleton.haskey == 1 and hero.haskey == 0:
                hero.getkey()
        else:
            pass
    elif hero.x == skeleton2.xx and hero.y == skeleton2.yy:
        if hero.sp > skeleton2.mdp:
            skeleton2.striked(hero.sp)
            if skeleton2.chp > 0:
                hero.striked(skeleton2.msp)
            elif skeleton2.haskey == 1 and hero.haskey == 0:
                hero.getkey()
        else:
            pass
    elif hero.x == skeleton3.xx and hero.y == skeleton3.yy:
        if hero.sp > skeleton3.mdp:
            skeleton3.striked(hero.sp)
            if skeleton3.chp > 0:
                hero.striked(skeleton3.msp)
            elif skeleton3.haskey == 1 and hero.haskey == 0:
                hero.getkey()
        else:
            pass
    elif hero.x == boss.xx and hero.y == boss.yy:
        if hero.sp > boss.dp:
            boss.striked(hero.sp)
            if boss.hp > 0:
                hero.striked(boss.sp)
        else:
            pass

def leftKey(event):
    left_pos = (hero.x - 1, hero.y)
    if hero.x == 0 or left_pos in wall:
        hero.move(x=0)
    else:
        hero.move(x=-1)
        hero.img = "hero_left"
    global counter
    counter += 1
    if counter == 2:
        skeleton.auto_move()
        skeleton2.auto_move()
        skeleton3.auto_move()
        boss.auto_move()
        counter = 0
def rightKey(event):

    right_position = (hero.x + 1, hero.y)
    if hero.x == 9 or right_position in wall:
        hero.move(x=0)
    else:
        hero.move(x=1)
        hero.img = "hero_right"
    global counter
    counter += 1
    if counter == 2:
        skeleton.auto_move()
        skeleton2.auto_move()
        skeleton3.auto_move()
        boss.auto_move()
        counter = 0


def upKey(event):

    upper_position = (hero.x, hero.y - 1)
    if hero.y == 0 or upper_position in wall:
        hero.move(y=0)
    else:
        hero.move(y=-1)
        hero.img = "hero_up"
    global counter
    counter += 1
    if counter == 2:
        skeleton.auto_move()
        skeleton2.auto_move()
        skeleton3.auto_move()
        boss.auto_move()
        counter = 0


def downKey(event):
    down_position = (hero.x, hero.y + 1)
    if hero.y == 9 or down_position in wall:
        hero.move(y=0)
    else:
        hero.move(y=1)
        hero.img = "hero_down"
    global counter
    counter += 1
    if counter == 2:
        skeleton.auto_move()
        skeleton2.auto_move()
        skeleton3.auto_move()
        boss.auto_move()
        counter = 0

def next_round():
    global filename
    global map_array
    if skeleton.chp == 0 and skeleton2.chp == 0 and skeleton3.chp ==  0 and boss.hp == 0 and hero.haskey == 1 and hero.x == 9 and hero.y == 9:
        filename = f"map{hero.lvl}.txt"
        with open(filename, 'r') as f:
            for line in f.readlines():
                map_array.append(line)
        draw_map()
        hero.lvl_up()
        skeleton.lvl_up()
        skeleton2.lvl_up()
        skeleton3.lvl_up()
    else:
        pass

root.bind('<Left>', leftKey)
root.bind('<space>', spaceBar)
root.bind('<Right>', rightKey)
root.bind('<Up>', upKey)
root.bind('<Down>', downKey)

# Don't write anything after this while loop, because that won't be executed
# The main game loop, at the moment it calls the draw_screen function continuously
while True:
    draw_map()
    next_round()
    show_stats()
    battle_stats()
    root.update_idletasks()
    root.update()
