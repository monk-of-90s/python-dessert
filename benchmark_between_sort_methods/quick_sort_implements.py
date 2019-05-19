def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    # middle-three 方法，选取首尾中三点中的中点作为pivotvalue
    first_item = alist[first]
    last_item = alist[last]
    middle_item = alist[(last + first) // 2]
    if first_item <= last_item <= middle_item or middle_item <= last_item <= first_item:
        pivotvalue = last_item
        alist[first], alist[last] = alist[last], alist[first]
    elif first_item <= middle_item <= last_item or last_item <= middle_item <= first_item:
        pivotvalue = middle_item
        alist[(last + first) // 2], alist[first] = alist[first], alist[(last + first) // 2]
    else:
        pivotvalue = first_item
    # # 选取middle作为pivotvalue
    # pivotvalue = alist[(last + first) // 2]
    # alist[(last + first) // 2], alist[first] = alist[first], alist[(last + first) // 2]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


if __name__ == '__main__':
    alist = [6, 5, 2, 8, 9, 12, 43, 8, 23, 32, 12]
    quickSort(alist)
    print(alist)
