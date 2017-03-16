from player import Player
from wall import Wall
from door_win import DoorWin
from ques import Ques
import random


class Map:
    dx_random = random.randrange(-1, 2, 1)
    dy_random = random.randrange(-1, 2, 1)

    def __init__(self, map_input, ques_input):
        self.width = len(map_input)
        self.height = len(map_input[0]) - 1
        self.wall = []
        self.ques = []
        check_ques = [True] * len(ques_input)
        for y in range(self.height):
            for x in range(self.width):
                if map_input[y][x] == "P":
                    self.player = Player(x, y)
                elif map_input[y][x] == "D":
                    self.door_win = DoorWin(x, y)
                elif map_input[y][x] == "#":
                    self.wall.append(Wall(x, y))
                elif map_input[y][x] == "Q":
                    while True:
                        index_ques = random.randint(0, len(ques_input)-1)
                        if check_ques[index_ques]:
                            break
                    self.ques.append(Ques(x, y, ques_input[index_ques]))
                    check_ques[index_ques] = False

    def in_map(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def find_wall(self, x, y):
        for i in range(len(self.wall)):
            if self.wall[i].match(x, y):
                return i
        return None

    def find_ques(self, x, y):
        for i in range(len(self.ques)):
            if self.ques[i].match(x, y):
                return i
        return None
