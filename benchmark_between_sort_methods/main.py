import timeit
import matplotlib.pyplot as plt

from benchmark_between_sort_methods import bubble_sort, merge_sort, quick_sort_implements, selection_sort, shell_sort, \
    insertion_sort

# 绘图横轴
lengths = []
# 绘图纵轴
times_bubble = []
times_merge = []
times_quick = []
times_selection = []
times_shell = []
times_insertion = []
# 测试实例
t = timeit.Timer('sort(alist)', 'from __main__ import sort,alist')
for length in range(100, 5001, 100):
    lengths.append(length)

    alist = list(range(length, 0, -1))
    # bubble
    sort = bubble_sort.shortBubbleSort
    times_bubble.append(t.timeit(2))
    # merge
    sort = merge_sort.mergeSort
    times_merge.append(t.timeit(2))
    # quick
    sort = quick_sort_implements.quickSort
    times_quick.append(t.timeit(2))
    # selection
    sort = selection_sort.selectionSort
    times_selection.append(t.timeit(2))
    # shell
    sort = shell_sort.shellSort
    times_shell.append(t.timeit(2))
    # insertion
    sort = insertion_sort.insertionSort
    times_insertion.append(t.timeit(2))

plt.plot(lengths, times_bubble, 'o', label='bubble')
plt.plot(lengths, times_shell, 'o', label='shell')
plt.plot(lengths, times_selection, 'o', label='selection')
plt.plot(lengths, times_quick, 'o', label='quick')
plt.plot(lengths, times_merge, 'o', label='merge')
plt.plot(lengths,times_insertion,'o',label='insertion')
plt.legend()
plt.show()
