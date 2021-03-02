import pygame as pg
import math
import pudb


class PygameController:

    def __init__(self):
        pg.init()
        self.win = pg.display.set_mode((820, 820))
        self.side = 195
        pg.key.set_repeat(0)
        self.RED = (200, 0, 0)
        self.font = pg.font.SysFont('Arial', 50)

    def color_selector(self, val):
        colors = [(239, 217, 206),
                  (222, 192, 241),
                  (183, 156, 237),
                  (149, 127, 239),
                  (113, 97, 239),
                  (47, 102, 144),
                  (22, 48, 91),
                  (71, 106, 111)]
        return colors[int(math.log(val, 2)) % len(colors)]

    def draw(self, table):
        for y in range(4):
            for x in range(4):
                unit = pg.Rect((10+(x*195), 10+(y*195), 195, 195))
                pg.draw.rect(self.win, (50, 0, 150) if table[y][x] == 0 else self.color_selector(
                    table[y][x]), unit, width=0)
                pg.draw.rect(self.win, self.RED, unit, width=1)
                text_surface = self.font.render(
                    str(table[y][x] if not table[y][x] == 0 else ""), True, self.RED)
                text_rect = text_surface.get_rect()
                text_rect.center = unit.center
                self.win.blit(text_surface, text_rect)

        pg.display.flip()

    def event_loop(self, run):
        direction = ""
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                run = -1
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    direction = "UP"
                elif event.key == pg.K_s:
                    direction = "DOWN"
                elif event.key == pg.K_d:
                    direction = "RIGHT"
                elif event.key == pg.K_a:
                    direction = "LEFT"

        return run, direction
