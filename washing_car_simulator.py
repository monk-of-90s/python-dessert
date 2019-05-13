import random

from pythonds import Queue


class Car:
    def __init__(self):
        self.wash_time = random.Random().randrange(60, 120)  # 根据车型不同，洗车时间在600-1200秒之间
        self.timestamp = -1


class Washer:
    def __init__(self):
        self.current_car_time = 0  # 当前被洗车辆剩下的时间

    # 调用一次洗一秒
    def wash(self, car: Car):
        # 无车在洗
        if car == None:
            return False
        # 开始洗车
        if self.current_car_time == 0:
            self.current_car_time = car.wash_time
        # 洗一秒
        self.current_car_time -= 1
        if self.current_car_time == 0:
            return False  # 洗完需要换车
        else:
            return True


washer = Washer()
car_queue = Queue()  # 洗车排队，只有10个车位
current: Car = None  # 空档状态
wait_time = []
# 模拟两小时
randomor = random.Random()
for second in range(7200):
    if randomor.randrange(600) == 0 and car_queue.size() < 20:  # 概率上600秒来一辆车,概率运算一定会一直进行
        new_car = Car()
        new_car.timestamp = second  # 标记开始等待时间
        car_queue.enqueue(new_car)  # 排到队尾

    # 洗车
    # if washer.current_car_time == 0 and not car_queue.isEmpty():  # 无车在洗,队列有车
    #     current = car_queue.dequeue()  # 队尾为下一个车
    if not washer.wash(current):  # 无车在洗
        if not car_queue.isEmpty():  # 有车可换
            current = car_queue.dequeue()
            wait_time.append(second - current.timestamp)  # 存储车辆等待时间
        else:  # 无车可换
            current = None

print('总共洗车：', len(wait_time), '辆，平均等待时间:', sum(wait_time) / len(wait_time), ",还剩", car_queue.size(), '辆车没洗')
