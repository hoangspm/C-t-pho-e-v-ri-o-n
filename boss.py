class Boss:
    def __init__(self, x, y, moverd):
        self.x = x
        self.y = y
        self.mv = moverd

    def print(self):
        print(self.x, self.y)

    def random_move(self):
        dx = [-1, 0, 1]
        dy = [-1, 0, 1]


    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def calc_next(self, dx, dy):
        return (self.x + dx), (self.y + dy)

    def match(self, x, y):
        return self.x == x and self.y == y