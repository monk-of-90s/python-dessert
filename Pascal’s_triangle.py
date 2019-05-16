def Pascal_triangle(row: int):
    if row == 1:
        return '1'
    else:
        above = Pascal_triangle(row - 1)
        # # 倒序
        # above = above[::-1]
        # 找到倒数第一个'\n'
        pos = above.rfind('\n')
        # 截取
        if pos >= 0:
            last_row = above[pos + 1:]
        else:
            last_row = above
        # 存储进list
        last_nums = [int(i) for i in last_row.split()]
        current_row = [last_nums[i] + last_nums[i + 1] for i in range(len(last_nums)) if i < len(last_nums) - 1]
        current_row.append(1)
        current_row.insert(0, 1)
        # above集体缩进
        above = '  ' + above
        above = above.replace('\n', '\n  ')
        return above+ '\n' + '   '.join([str(i) for i in current_row])


print(Pascal_triangle(8))
