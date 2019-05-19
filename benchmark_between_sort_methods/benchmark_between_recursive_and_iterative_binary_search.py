'''
binary search的recursive实现和iterative实现的比较
'''
# 绘图横轴
import timeit
import binary_search
import matplotlib.pyplot as plt

lengths = []
# 绘图纵轴
# recursive
times0 = []
# iterative
times1 = []
t = timeit.Timer('search(alist,item)', 'from __main__ import search,alist,item')
for length in range(10000, 1000001, 20000):
    lengths.append(length)

    alist = list(range(length))
    item = alist[length // 2]
    # recursive
    search = binary_search.binarySearch_recursive
    times0.append(t.timeit(1000))

    # iterative
    search = binary_search.binarySearch_iterative
    times1.append(t.timeit(1000))

plt.plot(lengths, times0, 'o', label='recursive')
plt.plot(lengths, times1, 'o', label='iterative')
plt.legend()
plt.show()
