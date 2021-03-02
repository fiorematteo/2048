import Game
import PygameController
import pudb


def recursive(fakeGame, direction, score, free_coord, depth):
    if depth < 7:
        scores = []
        if not free_coord[0] == None:
            fakeGame.table[free_coord[0]][free_coord[1]] = 2
        tmpTable = [row[:] for row in fakeGame.table]
        score = fakeGame.move(direction, score)
        validMove = False
        for y in range(4):
            for x in range(4):
                if fakeGame.table[y][x] != tmpTable[y][x]:
                    validMove = True
                    break
        if not validMove and not direction == "":
            score = -1000
            depth = 1000
        for free_coord in fakeGame.free_coords():
            for direction in ['UP','DOWN','LEFT','RIGHT']:
                tmpTable = [row[:] for row in fakeGame.table]
                fakeGame = Game.Game()
                fakeGame.table = tmpTable
                scores.append(recursive(fakeGame, direction, score, free_coord, depth+1)[0])
            return max(scores), free_coord
    return score, free_coord

def AI():
    output = []
    directions = ['UP','DOWN','LEFT','RIGHT']
    for direction in directions:
        tmpTable = [row[:] for row in game.table]
        fakeGame = Game.Game()
        fakeGame.table = tmpTable
        output.append(recursive(fakeGame, direction, 0, [None], 0))

    scores = [x[0] for x in output]
    index = scores.index(max(scores))
    return directions[index], output[index][1]


game = Game.Game()
controller = PygameController.PygameController()
run = 0
score = 0

game.new_rand()
game.new_rand()

while run == 0:
    run = game.game_over()

    run, direction = controller.event_loop(run)
    direction, free_coord = AI()
    print(f"direzione = {direction}".ljust(20)+f" | nuovo 2 = {free_coord}".ljust(20))

    if not direction == "":
        old_table = [row[:] for row in game.table]
        score = game.move(direction, score)
        abort = True
        for y in range(4):
            for x in range(4):
                if not game.table[y][x] == old_table[y][x]:
                    abort = False
                    break

        if not abort:
        #    game.new_rand()
            game.table[free_coord[0]][free_coord[1]] = 2
        direction = ""

    controller.draw(game.table)

print("GAME OVER" if run == -1 else "YOU WIN GAMER")
