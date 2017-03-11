def init_ques():
    myfile = open("ques.txt", "r")
    count_line = 0
    ques_input = []
    temp = {}
    ques_key = ["ques","a","b","c","d", "answer"]

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
    myfile = open("map.txt", "r")
    map_input = []
    while True:
        theline = myfile.readline()
        if len(theline) == 0:
            break
        map_input.append(theline)
    return map_input

ques_input = init_ques()
map_input = init_map()
for i in map_input:
    print(i)

map = Map(map_input,ques_input)