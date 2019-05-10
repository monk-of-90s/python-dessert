import random, draw_queens2


def has_clashs(queen: list) -> bool:
    length = len(queen)
    for row, col in enumerate(queen):
        # column check
        row_index, col_index = 0, 0
        for row_index in range(length):
            if row_index != row and queen[row_index] == col:
                return True
        # right down line check
        row_index, col_index = 0, 0
        while 0 <= row_index < length and 0 <= col_index < length:
            col_index = col + row_index - row
            if not (row_index == row and col_index == col):
                if queen[row_index] == col_index:
                    return True
            row_index += 1
            col_index = 0
        # left down line check
        row_index, col_index = 0, 0
        while 0 <= row_index < length and 0 <= col_index < length:
            col_index = col + row - row_index
            if not (row_index == row and col_index == col):
                if queen[row_index] == col_index:
                    return True
            row_index += 1
            col_index = 0

    return False


assert not has_clashs([0, 5, 3, 1, 6, 4, 2])
assert not has_clashs([6, 4, 2, 0, 5, 7, 1, 3])
assert not has_clashs([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1])
assert not has_clashs([11, 4, 8, 12, 2, 7, 3, 15, 0, 14, 10, 6, 13, 1, 5, 9])
assert has_clashs([0, 5, 3, 6, 1, 4, 2])
assert has_clashs([6, 4, 2, 0, 3, 7, 1, 5])
assert has_clashs([9, 6, 0, 3, 10, 1, 2, 4, 12, 8, 11, 5, 7])
assert has_clashs([11, 4, 0, 12, 2, 7, 3, 15, 8, 14, 10, 6, 13, 1, 5, 9])


def main():
    board = list(range(10))
    num_found = 0
    tries = 0
    while num_found < 10:
        random.shuffle(board)
        tries += 1
        if not has_clashs(board):
            print('Found solution {0} in {1} tries.'.format(board, tries))
            tries = 0
            draw_queens2.draw_board(board)
            num_found += 1


main()
