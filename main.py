from map import Map
import pygame
import random

dx_random = random.randrange(-1, 2, 1)
dy_random = random.randrange(-1, 2, 1)


def init_ques():
    myfile = open("ques.txt", "r")
    count_line = 0
    ques_input = []
    temp = {}
    ques_key = ["ques", "a", "b", "c", "d", "answer"]

    while True:
        theline = myfile.readline()
        if len(theline) == 0:
            break
        temp[ques_key[count_line]] = theline
        if count_line == 5:
            ques_input.append(temp)
            temp = {}
        count_line = (count_line + 1) % 6
    myfile.close()
    return ques_input


def init_map():
    myfile = open("map1.txt", "r")
    map_input = []
    while True:
        theline = myfile.readline()
        if len(theline) == 0:
            break
        map_input.append(theline)
    myfile.close()
    return map_input


def print_game(map):
    screen.fill(COLOR_BLACK)
    for y in range(map.height):
        for x in range(map.width):
            screen.blit(plattform_image, (x * square_size, y * square_size))
            if map.player.match(x, y):
                screen.blit(player_image, (x*square_size, y*square_size))
            elif map.door_win.match(x, y):
                screen.blit(door_win_image, (x * square_size, y*square_size))
            elif map.find_wall(x, y) != None:
                screen.blit(wall_image, (x * square_size, y * square_size))
            elif map.find_ques(x, y) != None:
                screen.blit(ques_image, (x * square_size, y * square_size))
    pygame.display.flip()

ques_input = init_ques()
map_input = init_map()
pygame.init()
screen = pygame.display.set_mode([800, 600])
COLOR_BLACK = (0, 0, 0)
player_image = pygame.image.load("images/police man/police_right.png")
wall_image = pygame.image.load("images/wall_x.png")
ques_image = pygame.image.load("images/ques.jpg")
door_win_image = pygame.image.load("images/door_win.png")
plattform_image = pygame.image.load("images/plattform.jpg")
square_size = 40

map = Map(map_input, ques_input)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    print_game(map)
    pygame.display.flip()
