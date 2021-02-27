import random as rn


class Game:

    def __init__(self):
        self.table = []
        for y in range(4):
            self.table.append([])
            for x in range(4):
                self.table[y].append(0)

    def game_over(self):
        for y in range(4):
            for x in range(4):
                if self.table[y][x] == 2048:
                    return 1

        for y in range(4):
            for x in range(4):
                if self.table[y][x] == 0:
                    return 0

        for y in range(4):
            for x in range(4):
                if y + 1 <= 3 and self.table[y][x] == self.table[y+1][x]:
                    return 0
                if x + 1 <= 3 and self.table[y][x] == self.table[y][x+1]:
                    return 0
                if x - 1 >= 0 and self.table[y][x] == self.table[y-1][x]:
                    return 0
                if x - 1 >= 0 and self.table[y][x] == self.table[y][x-1]:
                    return 0

        return -1

    def collision(self, arr, score):
        i = 3
        while i > 0:
            if arr[i] == arr[i-1]:
                score += arr[i]
                arr[i] *= 2
                arr[i-1] = 0
            if not arr[i] == 0 and i + 1 <= 3 and arr[i+1] == 0:
                arr[i+1] = arr[i]
                arr[i] = 0
            i -= 1
        if not arr[0] == 0 and arr[1] == 0:
            arr[1] = arr[0]
            arr[0] = 0
        return (arr, score)

    def new_rand(self):
        free_coords = []
        y = 0
        while y <= 3:
            x = 0
            while x <= 3:
                if self.table[y][x] == 0:
                    free_coords.append((y, x))
                x += 1
            y += 1

        index = free_coords[rn.randint(0, len(free_coords)-1)]
        self.table[index[0]][index[1]] = 4 if rn.randint(0, 9) == 0 else 2

    def move_vertical(self, dir, score):
        x = 0
        while x < 4:
            y = 0 if dir == 1 else 3
            while (y <= 3 and dir == 1)or(y >= 0 and dir == -1):
                if not self.table[y][x] == 0:
                    if y + dir >= 0 and y + dir <= 3 and self.table[y+dir][x] == 0:
                        self.table[y+dir][x] = self.table[y][x]
                        self.table[y][x] = 0
                        y = 0 if dir == 1 else 3
                        continue
                y += dir
            x += 1

        x = 0
        while x < 4:
            arr = []
            y = 0 if dir == 1 else 3
            while (y <= 3 and dir == 1)or(y >= 0 and dir == -1):
                arr.append(self.table[y][x])
                y += dir
            arr, score = self.collision(arr, score)
            i = 0
            y = 0 if dir == 1 else 3
            while (y <= 3 and dir == 1)or(y >= 0 and dir == -1):
                self.table[y][x] = arr[i]
                y += dir
                i += 1
            x += 1
        return score

    def move_horizontal(self, dir, score):
        y = 0
        while y < 4:
            x = 0 if dir == 1 else 3
            while (x <= 3 and dir == 1)or(x >= 0 and dir == -1):
                if not self.table[y][x] == 0:
                    if x + dir >= 0 and x + dir <= 3 and self.table[y][x+dir] == 0:
                        self.table[y][x+dir] = self.table[y][x]
                        self.table[y][x] = 0
                        x = 0 if dir == 1 else 3
                        continue
                x += dir
            y += 1

        y = 0
        while y < 4:
            arr = []
            x = 0 if dir == 1 else 3
            while (x <= 3 and dir == 1)or(x >= 0 and dir == -1):
                arr.append(self.table[y][x])
                x += dir
            arr, score = self.collision(arr, score)
            i = 0
            x = 0 if dir == 1 else 3
            while (x <= 3 and dir == 1)or(x >= 0 and dir == -1):
                self.table[y][x] = arr[i]
                x += dir
                i += 1
            y += 1
        return score

    def move(self, dir, score):
        if dir == "UP":
            return self.move_vertical(-1, score)
        elif dir == "DOWN":
            return self.move_vertical(1, score)
        elif dir == "RIGHT":
            return self.move_horizontal(1, score)
        elif dir == "LEFT":
            return self.move_horizontal(-1, score)
