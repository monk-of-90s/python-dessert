from pythonds import Queue


def radix_sorting_machine(num_list: list) -> list:
    # main_bin 设定
    main_bin = Queue()
    main_bin.items = num_list
    # 10个digit bin
    bin_dic = [None] * 10
    # 最大数字位计算
    max_digit = 0
    for i in num_list:
        current_len = len(str(i))
        if current_len > max_digit:
            max_digit = current_len
    # 逐位排序,便览各位
    for n in range(1, max_digit + 1):
        while not main_bin.isEmpty():  # 便览main_bin中的数
            current_num = main_bin.dequeue()
            current_num_copy = current_num
            # 计算倒数第n位的数字
            m = 1
            while m <= n:
                remainder = current_num_copy % 10
                current_num_copy = current_num_copy // 10
                m += 1
            # 存储进remainder号bin
            if bin_dic[remainder] == None:
                bin_dic[remainder]: Queue = Queue()
            bin_dic[remainder].enqueue(current_num)
            # 逐个digit bin弹出数字到main_bin
        for digit_bin in bin_dic:
            while digit_bin != None and not digit_bin.isEmpty():
                main_bin.enqueue(digit_bin.dequeue())

    return main_bin.items


print(radix_sorting_machine([4234, 53, 234, 6765, 32,10000,34,23,546,234,76,5,345]))
