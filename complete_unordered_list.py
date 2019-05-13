class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None
        self.num = 0

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.num += 1

    def append(self, item):
        current = self.head
        if current == None:
            self.head = Node(item)
        else:
            while current != None:
                previous = current
                current = current.getNext()
            previous.setNext(Node(item))
        self.num += 1

    def __len__(self):
        return self.num

    def __str__(self):
        s = []
        current = self.head
        while current != None:
            s.append(current.getData())
            current = current.getNext()
        return str(s)

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def __getitem__(self, index):
        # 索引
        if isinstance(index, int):
            # 负数索引转换
            while index < 0:
                index += self.num
            # 便览
            current = self.head
            # 空列表特例
            if current == None:
                return None
            index -= 1
            while index >= 0 and current != None:
                current = current.getNext()
                index -= 1
            if index < 0 and current != None:
                return current.getData()
            # 切片
        elif isinstance(index, slice):
            slice_UnorderedList = UnorderedList()

            # 传递切片属性到可写变量
            step = 1 if index.step == None else index.step
            start = index.start
            if start != None:
                # 负数索引转换
                while start < 0:
                    start += self.num
            else:
                # 空缺索引转换
                start = 0 if step > 0 else self.num-1

            stop = index.stop
            if stop != None:
                # 负数索引转换
                while stop < 0:
                    stop += self.num
            else:
                # 空缺索引转换
                stop = self.num if step > 0 else -1

            # 索引序号检查
            if start > self.num or stop > self.num or start == stop:
                return slice_UnorderedList

            # 正步切片
            if step > 0:
                # 索引序号检查
                if start >= stop:
                    return slice_UnorderedList

                # 在原始链表中查找元素
                current = self.head
                temp_step = 0  # 步进计数
                while current != None and (start >= 0 or stop > 0):  # 此刻start stop表示还剩的步数
                    # 只在第一步获取之后开始计数
                    if not slice_UnorderedList.isEmpty():
                        temp_step += 1
                    # 第一步必获取
                    if start == 0:
                        slice_UnorderedList.append(current.getData())
                    # 步进完毕
                    if temp_step == step:
                        temp_step = 0
                        slice_UnorderedList.append(current.getData())
                    current = current.getNext()
                    start -= 1
                    stop -= 1
            # 负步切片
            elif step < 0:
                # 索引序号检查
                if start <= stop:
                    return slice_UnorderedList
                # 转换为正步切片
                new_step = -step
                new_stop = start + 1
                new_start = start
                while new_start - new_step > stop:
                    new_start -= new_step
                start = new_start
                stop = new_stop
                step = new_step
                # 正步切片，其中逆向存储元素
                # 在原始链表中查找元素
                current = self.head
                temp_step = 0  # 步进计数
                while current != None and (start >= 0 or stop > 0):  # 此刻start stop表示还剩的步数
                    # 只在第一步获取之后开始计数
                    if not slice_UnorderedList.isEmpty():
                        temp_step += 1
                    # 第一步必获取
                    if start == 0:
                        slice_UnorderedList.add(current.getData())
                    # 步进完毕
                    if temp_step == step:
                        temp_step = 0
                        slice_UnorderedList.add(current.getData())
                    current = current.getNext()
                    start -= 1
                    stop -= 1

            return slice_UnorderedList

    def index(self, item):
        current = self.head  # 从头开始
        n = -1
        while current != None:
            n += 1
            if current.getData() == item:
                return n
            current = current.getNext()

    def pop(self):
        current = self.head
        previous = None
        # 便览,直到current是最后一个元素
        while current != None and current.getNext() != None:
            previous = current
            current = current.getNext()
        # 空列表
        if previous == current == None:
            return None
        # 只有一个元素
        elif current != None and previous == None:
            self.head = None
            self.num -= 1
            return current.getData()
        else:
            previous.setNext(None)
            self.num -= 1
            return current.getData()

    def insert(self, index: int, item):
        current = self.head
        if self.head == None:  # 空列表无法插入
            return False
        previous = None
        # 便览列表，确保current是第index号元素
        while index != 0 and current.getNext() != None:
            previous = current
            current = current.getNext()
            index -= 1
        # 如果是因为到达列表结尾结束便览
        if index != 0:
            return False
        # 插入第0号元素
        elif previous == None:
            new_item = Node(item)
            new_item.setNext(self.head)
            self.head = new_item
            self.num += 1
            return True
        # 插入元素
        else:
            new_item = Node(item)
            previous.setNext(new_item)
            new_item.setNext(current)
            self.num += 1
            return True

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current == None:
                raise ValueError('Remove what is not in the list')
            elif current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.num -= 1


mylist = UnorderedList()
mylist.add(1)
mylist.add(2)
mylist.add(3)
mylist.add(4)
mylist.append(5)
mylist.append(6)
print(mylist)
print(mylist[:2:2])
