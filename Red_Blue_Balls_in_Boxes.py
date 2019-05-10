import random


class Box:
    def __init__(self, ball1: str, ball2: str):
        self.ball1 = ball1
        self.ball2 = ball2

    def pick_one_ball(self):
        rad = random.Random()
        balls = [self.ball1, self.ball2]
        rad.shuffle(balls)
        yield balls[0]
        yield balls[1]


box1 = Box('R', 'R')
box2 = Box('B', 'B')
box3 = Box('R', 'B')
boxs = [box1, box2, box3]
rd = random.Random()
count_first_red = 0
count_red_blue = 0
for i in range(1000):
    selected_box = rd.choice(boxs)
    pick = selected_box.pick_one_ball()
    if next(pick) == 'R':
        count_first_red += 1
        if next(pick) == 'B':
            count_red_blue += 1
print('首先拿出红球的次数：', count_first_red, '\n而后拿出篮球的次数:', count_red_blue, '\n概率：', count_red_blue / count_first_red)
