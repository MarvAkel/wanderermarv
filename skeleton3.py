import random

class Skeleton3:

    def __init__(self, x, y, w, z):
        list = ["0", "1"]
        self.xx = random.randint(x, y)
        self.yy = random.randint(w, z)
        self.mlvl = 1
        self.mhp = 2 * self.mlvl * self.roll_it()
        self.chp = self.mhp
        self.mdp = self.mlvl / 2 * self.roll_it()
        self.msp = self.mlvl * self.roll_it()
        self.img = "skeleton.png"
        self.haskey = random.choice(list)
        self.wall = [(1, 0), (2, 0), (6, 0), (2, 1), (5, 1), (6, 1), (0, 2), (4, 2), (5, 2), (8, 2), (3, 3), (7, 3),
                     (8, 3), (0, 4), (5, 4), (0, 5), (1, 5), (2, 5), (8, 5), (9, 5), (0, 6), (5, 6), (6, 6), (9, 6),
                     (4, 7), (5, 7), (0, 8), (1, 8), (4, 8), (6, 8)]
        self.possible = []
        self.possible_moves = ()

    def roll_it(self):
        roll = random.randint(1, 6)
        return roll

    def smove(self, x=0, y=0):
        self.xx += x
        self.yy += y

    def striked(self, strike_power):
        self.chp -= strike_power
        if self.chp < 0:
            self.chp = 0
            self.img = "soul.png"

    def skeleton_possible_moves(self):
        self.possible = []
        left_position = (self.xx - 1, self.yy)
        right_position = (self.xx + 1, self.yy)
        upper_position = (self.xx, self.yy - 1)
        down_position = (self.xx, self.yy + 1)
        if left_position not in self.wall and self.xx > 0:
            self.possible.append(left_position)
        else:
            pass
        if right_position not in self.wall and self.xx < 9:
            self.possible.append(right_position)
        else:
            pass
        if upper_position not in self.wall and self.yy > 0:
            self.possible.append(upper_position)
        else:
            pass
        if down_position not in self.wall and self.yy < 9:
            self.possible.append(down_position)
        else:
            pass
        return self.possible

    def auto_move(self):
        if self.chp > 0:
            x = self.skeleton_possible_moves()
            self.possible_moves = random.choice(x)
            self.xx = self.possible_moves[0]
            self.yy = self.possible_moves[1]

    def lvl_up(self):
        self.mlvl += 1
        self.mhp = 2 * self.mlvl * self.roll_it()
        self.chp = self.mhp
        self.mdp = self.mlvl / 2 * self.roll_it()
        self.msp = self.mlvl * self.roll_it()