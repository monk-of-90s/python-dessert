import math


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                iteror = self.rehash(hashvalue, len(self.slots))
                nextslot = next(iteror)
                while self.slots[nextslot] != None and \
                        self.slots[nextslot] != key:
                    nextslot = next(iteror)

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace
        length = len(self.slots)
        # 计算负载系数
        load_factor = len(self) / length
        # 在负载系数超过50%时扩大哈希表长度到下一个质数
        if load_factor > 0.5:
            # 计算下一个素数
            length += 1
            while True:
                is_prime = True
                for i in range(2, math.ceil(length ** 0.5) + 1):
                    if length / i == length // i:
                        is_prime = False
                        break
                if is_prime:
                    break
                else:
                    length += 1
            old_slots = self.slots
            old_data = self.data
            # 扩展
            self.slots = [None] * length
            self.data = [None] * length
            # 重新存储键值对
            for slot in old_slots:
                if slot != None:
                    self.put(slot, old_data[old_slots.index(slot)])

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, initial_hash, size):
        step = 1
        while True:
            yield (int(step) + initial_hash) % size
            step = (step ** 0.5 + 1) ** 2

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __delitem__(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                self.data[position] = None
                self.slots[position] = None

            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __len__(self):
        count = 0
        for item in self.data:
            if item != None:
                count += 1
        return count

    def __contains__(self, item):
        for key in self.slots:
            if item == key:
                return True


if __name__ == '__main__':
    H = HashTable()
    H[54] = "cat"
    # print(H.slots)
    # print(H.data)
    H[26] = "dog"
    # print(H.slots)
    # print(H.data)
    H[93] = "lion"
    # print(H.slots)
    # print(H.data)
    H[17] = "tiger"
    # print(H.slots)
    # print(H.data)
    H[77] = "bird"
    # print(H.slots)
    # print(H.data)
    H[31] = "cow"
    # print(H.slots)
    # print(H.data)
    H[44] = "goat"
    # print(H.slots)
    # print(H.data)
    H[55] = "pig"
    # print(H.slots)
    # print(H.data)
    H[20] = "chicken"
    print(H.slots)
    print(H.data)
    # del H[17]
    # print(H.slots)
    # print(H.data)
    #
    print(H[20])
    #
    # print(H[17])
    H[20] = 'duck'
    print(H[20])
    print(H.slots)
    print(H.data)
    # print(H[99])
    # print(44 in H)
