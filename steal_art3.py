import random


# 通过编号获取重量和价值
def item2weival(item: int):
    if item == 1:
        return (2, 3)
    elif item == 2:
        return (3, 4)
    elif item == 3:
        return (4, 8)
    elif item == 4:
        return (5, 8)
    elif item == 5:
        return (9, 10)


# 不断递归，存储可能的组合
# knapsack 包里已经有的编号列表
def steal_art(capacity: int = 20, knapsack=[], history=[]):  # history的元素是set的列表，每个set内容包含arts们的items
    # base case是装进一个之后不能再装了
    items_outside = [i for i in range(1, 6) if i not in knapsack]
    randomor = random.Random()
    randomor.shuffle(items_outside)
    # 计算剩余负重
    contain_left = capacity - sum({item2weival(item)[0] for item in knapsack})
    for item_outside in items_outside:
        # 假设装进item_outside之后包的剩余重量
        contain_left_test = contain_left - item2weival(item_outside)[0]
        if contain_left_test > 0:
            # 假设装进item_outside之后包外面的最轻艺术品的重量
            lightest_outside = min(
                [item2weival(item)[0] for item in [item for item in items_outside if item != item_outside]])
            # 装不下最轻的，说明是最后一个
            if contain_left_test < lightest_outside:
                # 检查历史
                if set(knapsack + [item_outside]) not in history:
                    # 记录历史
                    history.append(set(knapsack + [item_outside]))
                    # # 返回价值
                    # return sum([item2weival(item)[1] for item in knapsack + [item_outside]])
            else:  # 不是最后一个则递归
                steal_art(capacity, knapsack + [item_outside], history)
    # 首次调用函数的时候
    if knapsack == []:
        # 找个最有价值最轻的装包
        # 计算一个方案的价值总额
        value = lambda x: sum([item2weival(item)[1] for item in x])
        # 按最贵的组合排序
        history.sort(key=value, reverse=True)
        # 获取最贵的一个或数个组合
        valuest_history = [items_set for items_set in history if value(items_set) == value(history[0])]
        # 计算一个方案的重量
        weight = lambda x: sum([item2weival(item)[0] for item in x])
        # 找最轻的那个
        lightest_items_set = None
        for items_set in valuest_history:
            if lightest_items_set == None or weight(items_set) < weight(lightest_items_set):
                lightest_items_set = items_set
        return lightest_items_set


print(steal_art(20))
