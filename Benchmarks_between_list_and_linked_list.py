import timeit

import complete_unordered_list
import matplotlib.pyplot as plt

# 两个列表测试
t1 = timeit.Timer('some_list.append(1)', 'from __main__ import some_list')
# t2 = timeit.Timer('len(some_list)', 'from __main__ import some_list')
# 记录数据的列表
lengths = []  # 横轴 列表/链表长度
times1 = []  # 竖轴数据1：链表方法所用时间
times2 = []  # 竖轴数据2：列表方法所用时间
# 长度切换
for length in range(10000, 1000001, 20000):
    lengths.append(length)
    # unordered_list的长度填充
    some_list = complete_unordered_list.UnorderedList()
    for i in range(length):
        some_list.add(i)
    # 测试开始
    times1.append(t1.timeit(10))
    # 列表测试
    some_list = list(range(length))
    times2.append(t1.timeit(10))
# 绘图
plt.plot(lengths, times1, 'o', label='linked_list')
plt.plot(lengths,times2, 'o', label='common_list')
plt.legend()
plt.show()
