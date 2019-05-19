class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = [key]
            self.data[hashvalue] = [data]
        elif key not in self.slots[hashvalue]:
            self.slots[hashvalue].append(key)
            self.data[hashvalue].append(data)
        else:
            self.data[hashvalue][self.slots[hashvalue].index(key)] = data

    def hashfunction(self, key, size):
        return key % size

    def get(self, key):
        hashvalue = self.hashfunction(key, len(self.slots))
        if self.slots[hashvalue] != None and key in self.slots[hashvalue]:
            return self.data[hashvalue][self.slots[hashvalue].index(key)]

    def __delitem__(self, key):
        # 查找key
        hashvalue = self.hashfunction(key, len(self.slots))
        if self.slots[hashvalue] != None and key in self.slots[hashvalue]:
            # 删除对应数据
            del self.data[hashvalue][self.slots[hashvalue].index(key)]
            # 删除key
            del self.slots[hashvalue][self.slots[hashvalue].index(key)]

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


if __name__ == '__main__':
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    print(H.slots)
    print(H.data)
    del H[44]
    print(H[44])
    print(H.slots)
    print(H.data)


    # print(H[20])
    #
    # print(H[17])
    # H[20] = 'duck'
    # print(H[20])
    # print(H[99])
