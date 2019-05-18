def mergeSort(alist, start: int = -1, end: int = -1):
    if start == end == -1:
        start = 0
        end = len(alist)
    print("Splitting ", alist)
    if end - start > 1:
        mid = (end - start) // 2 + start
        left_start = start
        left_end = mid
        mergeSort(alist, left_start, left_end)

        right_start = mid
        right_end = end
        mergeSort(alist, right_start, right_end)

        i = start
        j = mid
        temp_list = []
        while i < mid and j < end:
            if alist[i] <= alist[j]:
                temp_list.append(alist[i])
                i = i + 1
            else:
                temp_list.append(alist[j])
                j = j + 1

        while i < mid:
            temp_list.append(alist[i])
            i = i + 1

        while j < end:
            temp_list.append(alist[j])
            j = j + 1
        # 存储进alist
        for item in temp_list:
            alist[start] = item
            start += 1

    print("Merging ", alist)


alist = [54, 26, 93, 17, 43, 23, 7, 65, 23, 201]
mergeSort(alist)
print(alist)
