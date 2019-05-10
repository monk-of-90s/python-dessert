import random
import time


def sudoku(twoDList: list, row=0, col=0):  # 单格数独查找
    # 对单格和单数进行数独判定
    def judge_ok(r, c, n):
        if n != 0:
            # 横竖检测
            for i in range(9):
                if i != c and twoDList[r][i] == n:
                    return False
                if i != r and twoDList[i][c] == n:
                    return False

            # 小九宫格检测
            if 0 <= r < 3:
                little_house_row_range = range(0, 3)
            elif 3 <= r < 6:
                little_house_row_range = range(3, 6)
            else:
                little_house_row_range = range(6, 9)

            if 0 <= c < 3:
                little_house_col_range = range(0, 3)
            elif 3 <= c < 6:
                little_house_col_range = range(3, 6)
            else:
                little_house_col_range = range(6, 9)
            for lr in little_house_row_range:
                for lc in little_house_col_range:
                    if lr != r and lc != c and twoDList[lr][lc] == n:
                        return False
            return True

    if row == col == 8:
        # 空值填空
        if twoDList[row][col] == 0:
            l = list(range(1, 10))
            random.Random().shuffle(l)
            for i in l:
                if judge_ok(row, col, i):
                    twoDList[row][col] = i
                    return True
            else:
                twoDList[row][col] = 0
                return False
        else:  # 已经有值则返回判定结果
            return judge_ok(row, col, twoDList[row][col])

    else:
        # 空值填空
        if twoDList[row][col] == 0:
            l = list(range(1, 10))
            random.Random().shuffle(l)
            for i in l:
                if judge_ok(row, col, i):
                    twoDList[row][col] = i
                    nextrow = -1
                    nextcol = -1
                    if col + 1 < 9:
                        nextrow = row
                        nextcol = col + 1
                    else:
                        nextrow = row + 1
                        nextcol = 0
                    if sudoku(twoDList, nextrow, nextcol):
                        return True
            else:
                twoDList[row][col] = 0
                return False
        else:  # 有值
            if judge_ok(row, col, twoDList[row][col]):  # 这一格符合九宫规则
                # 判定下一格
                nextrow = -1
                nextcol = -1
                if col + 1 < 9:
                    nextrow = row
                    nextcol = col + 1
                else:
                    nextrow = row + 1
                    nextcol = 0
                return sudoku(twoDList, nextrow, nextcol)


if __name__ == '__main__':

    L = [[0] * 9,
         [0] * 9,
         [0] * 9,
         [0] * 9,
         [0] * 9,
         [0] * 9,
         [0] * 9,
         [0] * 9,
         [0] * 9]
    sudoku(L)
    for i in range(9):
        print(L[i])
