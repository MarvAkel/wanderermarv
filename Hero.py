import random

class Hero:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.max_hp = 20 + 3 * self.roll_it()
        self.hp = self.max_hp
        self.dp = 2 * self.roll_it()
        self.sp = 5 + self.roll_it()
        self.img = "hero_down"
        self.lvl = 1
        self.round = 1
        self.haskey = 0

    def move(self, x = 0, y = 0):
        counter = 0
        self.x += x
        self.y += y
        prev_x = self.x
        if prev_x != self.x:
            counter += 1
            prev_x = self.x
        else:
            pass
        return counter

    def roll_it(self):
        roll = random.randint(1, 6)
        return roll

    def lvl_up(self):
        if self.round - self.lvl == "1":
            self.lvl += 1
            self.max_hp += self.roll_it()
            self.dp += self.roll_it()
            self.sp += self.roll_it()
        else:
            pass

    def striked(self, strike_power):
        self.hp -= strike_power
        if self.hp < 0:
            self.hp = 0

    def getkey(self):
        self.haskey = 1

    def level_up(self):
        self.lvl += 1
