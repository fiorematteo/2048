from Game import *
from PygameController import *
from pprint import pprint



game = Game()
controller = PygameController()
old_table = [row[:] for row in game.table]
run = 0
score = 0

game.new_rand()
game.new_rand()

while run == 0:
    run = game.game_over()

    run, abort, dir, game.table, old_table = controller.event_loop(game.table, old_table)

    if not dir == "":
        old_table = [row[:] for row in game.table]
        score = game.move(dir, score)
        abort = True
        for y in range(4):
            for x in range(4):
                if not game.table[y][x] == old_table[y][x]:
                    abort = False
                    break

        if not abort:
            game.new_rand()
        dir = ""

    controller.draw(game.table)

print("GAME OVER" if run == -1 else "YOU WIN GAMER")
