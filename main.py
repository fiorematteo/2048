import pygame as pg
import random as rn
from pprint import pprint
import pudb


def game_over():
    y = 0
    while y <= 3:
        x = 0
        while x <= 3:
            if table[y][x] == 0:
                return True
            x += 1
        y += 1


def collision(arr):
    i = 3
    while i > 0:
        if arr[i] == arr[i-1]:
            arr[i] *= 2
            arr[i-1] = 0
        if not arr[i] == 0 and i + 1 <= 3 and arr[i+1] == 0:
            arr[i+1] = arr[i]
            arr[i] = 0
        i -= 1
    if not arr[0] == 0 and arr[1] == 0:
        arr[1] = arr[0]
        arr[0] = 0
    return arr


def new_rand():
    free_coords = []
    y = 0
    while y <= 3:
        x = 0
        while x <= 3:
            if table[y][x] == 0:
                free_coords.append((y, x))
            x += 1
        y += 1

    index = free_coords[rn.randint(0, len(free_coords)-1)]
    table[index[0]][index[1]] = 4 if rn.randint(0, 9) == 0 else 2


def move_vertical(dir):
    x = 0
    while x < 4:
        y = 0 if dir == 1 else 3
        while (y <= 3 and dir == 1)or(y >= 0 and dir == -1):
            if not table[y][x] == 0:
                if y + dir >= 0 and y + dir <= 3 and table[y+dir][x] == 0:
                    table[y+dir][x] = table[y][x]
                    table[y][x] = 0
                    y = 0 if dir == 1 else 3
                    continue
            y += dir
        x += 1

    x = 0
    while x < 4:
        arr = []
        y = 0 if dir == 1 else 3
        while (y <= 3 and dir == 1)or(y >= 0 and dir == -1):
            arr.append(table[y][x])
            y += dir
        arr = collision(arr)
        i = 0
        y = 0 if dir == 1 else 3
        while (y <= 3 and dir == 1)or(y >= 0 and dir == -1):
            table[y][x] = arr[i]
            y += dir
            i += 1
        x += 1


def move_horizontal(dir):
    y = 0
    while y < 4:
        x = 0 if dir == 1 else 3
        while (x <= 3 and dir == 1)or(x >= 0 and dir == -1):
            if not table[y][x] == 0:
                if x + dir >= 0 and x + dir <= 3 and table[y][x+dir] == 0:
                    table[y][x+dir] = table[y][x]
                    table[y][x] = 0
                    x = 0 if dir == 1 else 3
                    continue
            x += dir
        y += 1

    y = 0
    while y < 4:
        arr = []
        x = 0 if dir == 1 else 3
        while (x <= 3 and dir == 1)or(x >= 0 and dir == -1):
            arr.append(table[y][x])
            x += dir
        arr = collision(arr)
        i = 0
        x = 0 if dir == 1 else 3
        while (x <= 3 and dir == 1)or(x >= 0 and dir == -1):
            table[y][x] = arr[i]
            x += dir
            i += 1
        y += 1


def move(dir):
    if dir == "UP":
        move_vertical(-1)
    elif dir == "DOWN":
        move_vertical(1)
    elif dir == "RIGHT":
        move_horizontal(1)
    elif dir == "LEFT":
        move_horizontal(-1)


pg.init()
padding = 10
win = pg.display.set_mode((800+2*padding, 800+2*padding))
side = (win.get_size()[0]-2*padding)/4
pg.key.set_repeat(0)
run = True

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0,  0)

table = []
for y in range(4):
    table.append([])
    for x in range(4):
        table[y].append(0)

font = pg.font.SysFont('Arial', 50)

new_rand()
new_rand()

while run:
    run = game_over()

    dir = ""  # UP DOWN LEFT RIGHT
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                dir = "UP"
            elif event.key == pg.K_s:
                dir = "DOWN"
            elif event.key == pg.K_d:
                dir = "RIGHT"
            elif event.key == pg.K_a:
                dir = "LEFT"

    if not dir == "":
        old_table = [row[:] for row in table]
        move(dir)
        abort = True
        y = 0
        while y <= 3:
            x = 0
            while x <= 3:
                if not table[y][x] == old_table[y][x]:
                    abort = False
                    break
                x += 1
            y += 1

        if not abort:
            new_rand()
        dir = ""

    y = 0
    while y < 4:
        x = 0
        while x < 4:
            unit = pg.Rect((padding+(x*side), padding+(y*side), side, side))
            pg.draw.rect(win,(min(10*table[y][x],255),100,100), unit, width=0)
            pg.draw.rect(win, GREEN, unit, width=1)
            text = pg.Rect(unit)
            win.blit(font.render(
                str(table[y][x]), True, GREEN), text.center)
            x += 1
        y += 1

    pg.display.flip()
print("GAME OVER SUCKER")
