import pygame as pg
import random as rn

pg.init()
padding = 10
win = pg.display.set_mode((800+2*padding, 800+2*padding))
pg.key.set_repeat(0)
run = True
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
side = (win.get_size()[0]-2*padding)/4

table = []
for y in range(4):
    table.append([])
    for x in range(4):
        table[y].append({"X": x, "Y": y, "value": 0})

font = pg.font.SysFont('Arial', 50)

new_rand()
new_rand()

while run:
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
    new_rand()

    y = 0
    while y < 4:
        x = 0
        while x < 4:
            unit = pg.Rect((padding+(x*side),padding+(y*side),side, side))
            pg.draw.rect(win, GREEN, unit, width=1)
            win.blit(font.render(str(table[y][x]["value"]), True, GREEN), unit.center)
            x += 1
        y += 1

    pg.display.flip()

def new_rand():
    a = rn.randint(1,2)
    y = rn.randint(0,3)
    x = rn.randint(0,3)

    table[y][x]["value"] = a
