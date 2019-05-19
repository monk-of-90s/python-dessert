def shortBubbleSort_2direction(alist):
    # 确定扫描的首尾
    head = 1
    end = len(alist)
    while head < end:
        # 变化
        change = False
        # 正向扫描
        for index in range(head, end):
            if alist[index] < alist[index - 1]:
                change = True
                alist[index], alist[index - 1] = alist[index - 1], alist[index]
        if not change:
            break
        end -= 1
        change = False
        # 逆向扫描
        for index in range(end - 1, head - 1, -1):
            if alist[index] < alist[index - 1]:
                change = True
                alist[index], alist[index - 1] = alist[index - 1], alist[index]
        if not change:
            break
        head += 1


if __name__ == '__main__':
    alist = [34, 32, 65, 2, 87, 23, 88, 65, 34, -8, 1, -5]
    shortBubbleSort_2direction(alist)
    print(alist)
