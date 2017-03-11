class Ques:
    def __init__(self,x,y,ques_input):
        self.x = x
        self.y = y
        self.ques = ques_input["ques"]
        self.a = ques_input["a"]
        self.b = ques_input["b"]
        self.c = ques_input["c"]
        self.d = ques_input["c"]
        self.answer = ques_input["answer"]

    def match(self,x,y):
        return self.x == x and self.y == y

    def check_answer(self,answer):
        return self.answer == answer.lower()