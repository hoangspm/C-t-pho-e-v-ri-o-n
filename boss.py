class Boss:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print(self.x, self.y)

    def move(self, dx_random, dy_random):
        self.x += dx_random
        if dx_random == 0:
            self.y += dy_random

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def calc_next(self, dx, dy):
        return (self.x + dx), (self.y + dy)

    def match(self, x, y):
        return self.x == x and self.y == y