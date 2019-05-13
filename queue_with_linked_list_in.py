from complete_unordered_list import UnorderedList


class Queue:
    def __init__(self):
        self.unordered_list = UnorderedList()

    def items(self):
        # 计算items
        items = []
        current = self.unordered_list.head
        # 便览链表元素
        while current != None:
            items.append(current.getData())
            current = current.getNext()
        return items

    def isEmpty(self):
        return self.unordered_list.isEmpty()

    def size(self):
        return self.unordered_list.size()

    def enqueue(self, item):
        self.unordered_list.append(item)

    def dequeue(self):
        res = self.unordered_list.head
        self.unordered_list.head = res.getNext()
        return res.getData()
