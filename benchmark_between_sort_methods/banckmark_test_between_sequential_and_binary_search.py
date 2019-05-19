'''banchmark test between a sequential search and a binary search
'''
import random
import matplotlib.pyplot as plt
import sequential_search, binary_search
import timeit

# 绘图横轴
lengths = []
# 绘图纵轴
times0 = []
times1 = []
t = timeit.Timer('search(alist,item)', 'from __main__ import alist,search,item')
for length in range(10000, 1000001, 20000):
    lengths.append(length)
    # 设置列表和查找条目
    alist = list(range(length))
    item = length // 2

    # sequential search
    search = sequential_search.sequentialSearch
    times0.append(t.timeit(10))

    # binary search
    search = binary_search.binarySearch_iterative
    times1.append(t.timeit(10))
    # print(lengths)
    # print(times0)
    # print(times1)
plt.plot(lengths, times0, 'o', label='sequential search')
plt.plot(lengths, times1, 'o', label='binary search')
plt.legend()
plt.show()
