import timeit
import matplotlib.pyplot as plt


def shellSort(alist, gap):
    sublistcount = gap
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        print("After increments of size", sublistcount,
              "The list is", alist)

        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


if __name__ == '__main__':
    # 绘图纵轴
    lengths = []
    # 绘图横轴
    times_3 = []
    times_4 = []
    times_5 = []
    times_6 = []
    # 测试器
    t = timeit.Timer('shellSort(alist,gap)', 'from __main__ import shellSort,alist,gap')
    for length in range(100, 5001, 100):
        lengths.append(length)

        alist = list(range(length, 0, -1))

        # gap 3
        gap = 3
        times_3.append(t.timeit(4))
        # gap 4
        gap = 4
        times_4.append(t.timeit(4))
        # gap 5
        gap = 5
        times_5.append(t.timeit(4))
        # gap 6
        times_6.append(t.timeit(4))
plt.plot(lengths, times_3, 'o', label='gap 3')
plt.plot(lengths, times_4, 'o', label='gap 4')
plt.plot(lengths, times_5, 'o', label='gap 5')
plt.plot(lengths, times_6, 'o', label='gap 6')
plt.legend()
plt.show()
