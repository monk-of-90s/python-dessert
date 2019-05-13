import complete_unordered_list


class Stack:
    def __init__(self):
        self.unordered_list = complete_unordered_list.UnorderedList()

    def items(self):
        # 计算items
        items = []
        current = self.unordered_list.head
        # 便览链表元素
        while current != None:
            items.append(current.getData())
            current = current.getNext()
        return items

    def size(self):
        return self.unordered_list.size()

    def isEmpty(self):
        return self.unordered_list.isEmpty()

    def pop(self):
        res = self.unordered_list.head
        self.unordered_list.head = res.getNext()
        return res.getData()

    def push(self, item):
        self.unordered_list.add(item)

    def peek(self):
        return self.unordered_list.head
