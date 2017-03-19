from map import Map
from wall import Wall
from pygame import Rect
import pygame

<<<<<<< HEAD
pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Prison Riot")
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
player_right_image = pygame.image.load("images/police man/police_right.png")
player_left_image = pygame.image.load("images/police man/police_left.png")
player_top_image = pygame.image.load("images/police man/police_top.png")
player_down_image = pygame.image.load("images/police man/police_down.png")
boss_image = pygame.image.load("images/prison/prison_right.png")
wall_image = pygame.image.load("images/wall_x.png")
ques_image = pygame.image.load("images/ques.jpg")
bg_ques_image = pygame.image.load("images/ques_1.png")
door_win_image = pygame.image.load("images/door_win.png")
plattform_image = pygame.image.load("images/plattform.jpg")
game_lost_image = pygame.image.load("images/murder.jpg")
game_win_image = pygame.image.load("images/victory.jpg")
story_1_image = pygame.image.load("images/story_1.jpg")
story_2_image = pygame.image.load("images/story2.jpg")
story_3_image = pygame.image.load("images/story3.jpg")
avatar_image = pygame.image.load("images/avatar.jpg")
clock_image = pygame.image.load("images/clock.png")
blood_image = pygame.image.load("images/blood.png")
pass_target_image = pygame.image.load("images/pass_target.png")
fail_target_image = pygame.image.load("images/failded_target.png")
square_size = 40
clock = pygame.time.Clock()
player_image = player_right_image


class TimeModel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_rect(self):
        return Rect(self.x, self.y)

clock_model = TimeModel(50, 50)
blood_model = TimeModel(695, 50)


def direct_move():
    if event.key == pygame.K_RIGHT:
        player_image = player_right_image
    elif event.key == pygame.K_DOWN:
        player_image = player_down_image
    elif event.key == pygame.K_LEFT:
        player_image = player_left_image
    elif event.key == pygame.K_UP:
        player_image = player_top_image
    else:
        player_image = player_right_image
    return player_image

=======
>>>>>>> 98ee8dd7c75667995495264417ec75379cc88ad0

def init_ques():
    myfile = open("ques.txt", "r")
    count_line = 0
    ques_input = []
    temp = {}
    ques_key = ["content", "a", "b", "c", "d", "answer"]
    while True:
        theline = myfile.readline()
        if len(theline) == 0:
            break
        temp[ques_key[count_line]] = theline[:len(theline)-1]
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


<<<<<<< HEAD
def min(a, b):
    if a > b:
        return b
    return a


def max(a, b):
    if a > b:
        return a
    return b
=======
def read_ques():
    if map.find_ques(map.player.x, map.player.y) != None:
        show = pygame.image.load("images/ques_1.png")
        screen.blit(show, (0, 100))
        myfont = pygame.font.SysFont("san_serif", 15)
        label = myfont.render("Some text!", 1, (255, 255, 0))
        screen.blit(label, (150, 250))
        pygame.display.flip()
        while True:
            ans = input("Your answer?:")
            if len(ans) != 0:
                break
>>>>>>> 98ee8dd7c75667995495264417ec75379cc88ad0


def print_game(map):
    for y in range(map.height):
        for x in range(map.width):
            screen.blit(plattform_image, (200 + (x * square_size), 100 + (y * square_size)))
            if map.player.match(x, y):
                screen.blit(player_image, (200 + (x * square_size), 100 + (y * square_size)))
            elif map.boss.match(x, y):
<<<<<<< HEAD
                screen.blit(boss_image, (200 + (x * square_size), 100 + (y*square_size)))
            elif map.door_win.match(x, y):
                screen.blit(door_win_image, (200 + (x * square_size), 100 + (y*square_size)))
=======
                screen.blit(boss_image, (200 + (x * square_size), 100 + (y * square_size)))
            elif map.door_win.match(x, y):
                screen.blit(door_win_image, (200 + (x * square_size), 100 + (y * square_size)))
>>>>>>> 98ee8dd7c75667995495264417ec75379cc88ad0
            elif map.find_wall(x, y) != None:
                screen.blit(wall_image, (200 + (x * square_size), 100 + (y * square_size)))
            elif map.find_ques(x, y) != None:
                screen.blit(ques_image, (200 + (x * square_size), 100 + (y * square_size)))
<<<<<<< HEAD
=======

>>>>>>> 98ee8dd7c75667995495264417ec75379cc88ad0
    pygame.display.flip()


def revert_content(content):
    step = 0
    b = []
    for i in range(len(content)):
        step += 1
        if content[i] == " " and step >= 65:
            b.append(content[i+1-step:i])
            step = 0
    b.append(content[i+1-step:i+1])
    return b


def show_ques(ques):
    myfont = pygame.font.SysFont("Arial Rounded MT Bold", 20)
    myfont_answer = pygame.font.SysFont("Arial Rounded MT Bold", 30)
    temp_content = revert_content(ques.content)
    content = []
    for temp in temp_content:
        content.append(myfont.render(temp, 1, COLOR_WHITE))
    choice_a = myfont.render(ques.a, 1, COLOR_WHITE)
    choice_b = myfont.render(ques.b, 1, COLOR_WHITE)
    choice_c = myfont.render(ques.c, 1, COLOR_WHITE)
    choice_d = myfont.render(ques.d, 1, COLOR_WHITE)
    your_answer = myfont_answer.render("YOUR ANSWER", 1, COLOR_WHITE)
    you_sure = myfont.render("ARE YOU SURE? PRESS [Y] or [N]", 1, COLOR_WHITE)

    def process_show_ques():
        screen.blit(bg_ques_image, (0, 100))
        for i in range(len(content)):
            screen.blit(content[i], (80, 215+i*25))
        screen.blit(choice_a, (90, 390))
        screen.blit(choice_b, (365, 390))
        screen.blit(choice_c, (90, 455))
        screen.blit(choice_d, (365, 455))
        screen.blit(your_answer, (40, 120))
    process_show_ques()
    pygame.display.flip()

    answer = "..."
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    answer = "A"
                elif event.key == pygame.K_b:
                    answer = "B"
                elif event.key == pygame.K_c:
                    answer = "C"
                elif event.key == pygame.K_d:
                    answer = "D"
                elif event.key == pygame.K_n:
                    answer = "..."
                elif event.key == pygame.K_y:
                    done = True
                    break
                else:
                    continue

            process_show_ques()
            answer_image = myfont_answer.render(answer, 1, COLOR_WHITE)
            screen.blit(answer_image, (205, 120))
            screen.blit(you_sure, (40, 150))
            pygame.display.flip()
    return ques.check_answer(answer)


def finish_ques(map, index_ques, result, request):
    if result:
        del map.ques[index_ques]
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    done = True
            screen.blit(pass_target_image, (0, 100))
            pygame.display.flip()
    else:
        del map.ques[index_ques]
        map.wall.append(Wall(map.player.x, map.player.y))
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    done = True
            screen.blit(fail_target_image, (0, 100))
            pygame.display.flip()

        dx, dy = 0, 0
        if request == pygame.K_UP:
            dy = -1
        elif request == pygame.K_DOWN:
            dy = +1
        elif request == pygame.K_LEFT:
            dx = -1
        elif request == pygame.K_RIGHT:
            dx = +1
        map.player.move(-dx, -dy)


def process_ques(map, request):
    index_ques = map.find_ques(map.player.x, map.player.y)
    if index_ques == None:
        return
    result = show_ques(map.ques[index_ques])
    finish_ques(map, index_ques, result, request)


def check_lost(map):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx*dy == 0:
                next_px, next_py = map.player.calc_next(dx, dy)
                if map.boss.match(next_px, next_py):
                    screen.fill(COLOR_WHITE)
                    screen.blit(game_lost_image, (0, 100))
                    myfont = pygame.font.SysFont("Arial Rounded MT Bold", 15)
                    replay_image = myfont.render("YOU DIED!!DO YOU WANT TO REPLAY??? [Y] or [N]", 1, COLOR_BLACK)
                    screen.blit(replay_image, (25, 550))
                    pygame.display.flip()
                    done = False
                    while not done:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                done = True
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:
                                    replay = True
                                    done = True
                                elif event.key == pygame.K_n:
                                    done = True
                    return True
    return False


def check_won(map):
    if map.door_win.match(map.player.x, map.player.y):
        screen.fill(COLOR_WHITE)
        screen.blit(game_win_image, (0, 100))
        myfont = pygame.font.SysFont("Arial Rounded MT Bold", 15)
        continue_image = myfont.render("DO YOU WANT TO NEXT LEVEL??? [Y] or [N]", 1, COLOR_BLACK)
        screen.blit(continue_image, (25, 450))
        pygame.display.flip()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        next_level = True
                        done = True
                    elif event.key == pygame.K_n:
                        done = True
        return True
    return False

ques_input = init_ques()
map_input = init_map()
<<<<<<< HEAD
map = Map(map_input, ques_input)
replay = False
done = False
next_level = False
timer_count = 0

list_intro = [story_1_image, story_2_image, story_3_image, avatar_image]
sound = pygame.mixer.Sound("Sounds/sound.wav")
pygame.mixer.Sound.play(sound)
for i in range(5):
    if i == 3:
        screen.blit(avatar_image, [0, 0])
        pygame.display.flip()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    done = True
                    break
    elif i == 4:
        done = False
        while not done:
            screen.fill(COLOR_BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    player_image = direct_move()
                    map.process_input(event.key)
                    process_ques(map, event.key)
                    if check_won(map):
                        continue
                    if check_lost(map):
                        continue
            timer_count += 1
            if timer_count >= 10:
                timer_count = 0
                clock_model.x += 1
            if clock_model.x == blood_model.x:
                done = True
                break

            screen.blit(clock_image, (clock_model.x, clock_model.y))
            screen.blit(blood_image, (blood_model.x, blood_model.y))
            print_game(map)
            clock.tick(80)
            pygame.display.flip()
    else:
        screen.blit(list_intro[i], (0, 100))
        pygame.display.flip()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    done = True
                    break

=======
pygame.init()
screen = pygame.display.set_mode([800, 600])
COLOR_BLACK = (0, 0, 0)
player_image = pygame.image.load("images/police man/police_right.png")
boss_image = pygame.image.load("images/prison/prison_right.png")
wall_image = pygame.image.load("images/wall_x.png")
ques_image = pygame.image.load("images/ques.jpg")
door_win_image = pygame.image.load("images/door_win.png")
plattform_image = pygame.image.load("images/plattform.jpg")
square_size = 40

map = Map(map_input, ques_input )

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            map.process_input(event.key)
            read_ques()

    print_game(map)
    pygame.display.flip()
>>>>>>> 98ee8dd7c75667995495264417ec75379cc88ad0
