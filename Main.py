import Game
import PygameController


def recursive(fakeGame, direction, score, free_coord, depth):
    if depth < 6:
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
            score -= 10
            depth = 100
        for free_coord in fakeGame.free_coords():
            for direction in ['UP','DOWN','LEFT','RIGHT']:
                fakeGame = Game.Game(fakeGame.table)
                scores.append(recursive(fakeGame, direction, score, free_coord, depth+1)[0])
            return max(scores), free_coord
    return score, free_coord

def AI():
    output = []
    directions = ['UP','DOWN','LEFT','RIGHT']
    for direction in directions:
        fakeGame = Game.Game(game.table)
        output.append(recursive(fakeGame, direction, 0, [None], 0))

    scores = [x[0] for x in output]
    index = scores.index(max(scores))
    return directions[index], output[index][1]


game = None
def main():
    global game;
    game = Game.Game()
    controller = PygameController.PygameController()
    run = 0
    score = 0
    lastMoves = []
    
    game.new_rand()
    game.new_rand()
    
    while run == 0:
        run = game.game_over()
    
        run, direction = controller.event_loop(run)
        direction, free_coord = AI()
    
        lastMoves.append(direction)
        if len(lastMoves) > 50:
            lastMoves.pop(0)
            if all(move == lastMoves[0] for move in lastMoves):
                run = -1
    
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
    
    print(f"score: {score}")
    print("GAME OVER" if run == -1 else "YOU WIN GAMER")

if __name__ == "__main__":
    main()
    input()
