import pygame
from map import Map

pygame.init()
screen = pygame.display.set_mode([800, 600])
square_image = pygame.image.load("square.png")
player_image = pygame.image.load("mario.png")
box_image = pygame.image.load("box.png")
tree_image = pygame.image.load("tree.png")
gate_image = pygame.image.load("gate.jpg")
win_image = pygame.image.load("win.jpg")
COLOR_WHITE = (255, 255, 255)
map = Map(20, 15)
square_size = 32

def print():
    screen.fill(COLOR_WHITE)
    for y in range(map.height):
        for x in range(map.width):
            if map.player.match(x, y):
                screen.blit(player_image, (x * square_size, y * square_size))
            elif map.box.match(x, y):
                screen.blit(box_image, (x * square_size, y * square_size))
            elif map.gate.match(x, y):
                screen.blit(gate_image, (x * square_size, y * square_size))
            elif map.find_tree(x, y) != None:
                screen.blit(tree_image, (x * square_size, y * square_size))
            else:
                screen.blit(square_image, (x * square_size, y * square_size))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
             map.process_input(event.key)
    print()
    if map.check_win():
        screen.blit(win_image, (0, 0))
    pygame.display.flip()
