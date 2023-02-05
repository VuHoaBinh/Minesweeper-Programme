import random
import utils
import global_vars as g

class Square():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.reset()

    def reset(self):
        self.is_bomb = False
        self.revealed = False
        self.bombs_around = 0

    def reveal(self):
        self.revealed = True
        return (self.is_bomb, self.bombs_around)

class Grid():
    def __init__(self):
        self.tab = [[Square(i, j) for j in range(g.WIDTH)] for i in range(g.HEIGHT)]

    def reset(self):
        for line in self.tab:
            for sq in line:
                sq.reset()

    def add_bombs(self):
        if g.BOMBS <= 0 or g.BOMBS >= g.HEIGHT*g.WIDTH:
            raise Exception("Invalid number of bombs.")
        else:
            pos = random.sample([(i, j) for j in range(g.WIDTH)for i in range (g.HEIGHT)], g.BOMBS)
            for (i, j) in pos:
                self.tab[i][j].is_bomb = True
                for (i2, j2) in utils.neighbours(i, j):
                    self.tab[i2][j2].bombs_around += 1

    def disp(self):
        for line in self.tab:
            for sq in line:
                if sq.is_bomb:
                    print('.', end='')
                else:
                    print(sq.bombs_around, end='')
            print()



