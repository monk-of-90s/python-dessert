import timeit
import matplotlib.pyplot as plt
from pythonds import Stack
from queue_with_linked_list_in import Queue

t1 = timeit.Timer('some_collection.push(1)', 'from __main__ import some_collection')
t2 = timeit.Timer('some_collection.enqueue(1)', 'from __main__ import some_collection')
# 记录数据的列表
lengths = []  # 横轴 collection长度
times1 = []  # 竖轴数据1：stack方法所用时间
times2 = []  # 竖轴数据2：queue方法所用时间
# 长度切换
for length in range(10000, 1000001, 20000):
    lengths.append(length)
    # some_collection的长度填充
    some_collection = Stack()
    some_collection.items = list(range(length))
    # 测试开始
    times1.append(t1.timeit(10))
    # queue测试
    some_collection = Queue()
    for i in range(length):
        some_collection.enqueue(i)
    times2.append(t2.timeit(10))
# 绘图
plt.plot(lengths, times1, 'o', label='linked_list')
plt.plot(lengths, times2, 'o', label='common_list')
plt.legend()
plt.show()
