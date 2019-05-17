# 计算最小Eidt Distance，通过三种操作：删除字母、插入、替换字母原字符串
# 简化为删除字母、插入（替换可视为删除和插入两个步骤）。
def smallest_edit_distance(from_s: str, to_s: str, pos: int = 0,
                           history={}) -> None:  # history存储中间的操作状态，key是中间状态的字符串，value是
    # base case
    # 两个字符串相等
    if from_s == to_s:
        return 0
    # 递归情况
    else:
        # 两个字符串当前字母相等
        if pos < len(from_s) and pos < len(to_s) and from_s[pos] == to_s[pos]:
            # # 上个步骤到目标字符串的步数
            # from_s_step = 0 if from_s not in history.keys() else history[from_s]
            next_from_s = from_s
            # 当前步数
            from_s_step = smallest_edit_distance(next_from_s, to_s, pos + 1, history)+0
            # 存储记录,到目标字符串的步骤
            if from_s in history.keys():
                if from_s_step < history[from_s]:
                    history[from_s] = from_s_step
            else:
                history[from_s] = from_s_step

            # # 接下来的步骤数
            # do_0_res = smallest_edit_distance(next_from_s, to_s, pos + 1, history)
        else:
            # 1、删除
            if pos < len(from_s):
                # # 上个步骤的步数
                # from_s_step = 0 if from_s not in history.keys() else history[from_s]
                next_from_s = from_s[:pos] + from_s[pos + 1:]
                # 接下来的步骤数
                from_s_step = smallest_edit_distance(next_from_s, to_s, pos, history) + 1

                # 存储记录,到目标字符串的步骤
                if from_s in history.keys():
                    if from_s_step < history[from_s]:
                        history[from_s] = from_s_step
                else:
                    history[from_s] = from_s_step

                # # 接下来的步骤数
                # del_res = smallest_edit_distance(next_from_s, to_s, pos, history)
            # 2、插入
            if pos <= len(from_s) and pos < len(to_s):
                # # 上个步骤的步数
                # from_s_step = 0 if from_s not in history.keys() else history[from_s]
                next_from_s = from_s[:pos] + to_s[pos] + from_s[pos:]
                # 当前步数
                from_s_step = smallest_edit_distance(next_from_s, to_s, pos + 1, history) + 1
                # 存储记录,到目标字符串的步骤
                if from_s in history.keys():
                    if from_s_step < history[from_s]:
                        history[from_s] = from_s_step
                else:
                    history[from_s] = from_s_step
        return history[from_s]

    return len(from_s) + len(to_s)


print(smallest_edit_distance('dhaa', 'ahds'))
#
# # 处理from_s最后一个字母
# # 删除字母
# if from_s[:-1] == to_s:
#     # 检索历史步骤数
#     if from_s in history.keys():
#         # 存储最小ED
#         if from_s[:-1] in history.keys():
#             if history[from_s] + 1 < history[from_s[:-1]]:
#                 history[from_s[:-1]] = history[from_s] + 1
#         else:
#             history[from_s[:-1]] = history[from_s] + 1
#     else:
#         return 1
# # 插入字母
# elif from_s + to_s[-1] == to_s:
#     # 检索历史步骤数
#     if from_s in history.keys():
#         # 存储最小ED
#         if
