class HashTable:
    def __init__(self, size):
        self.size = size
        self.hashmap = [None for _ in range(self.size)]
    
    def _hashing_funtion(self, key):
        hashed_key = 0
        
        for i in range(0, len(key)):
            hashed_key = (hashed_key + ord(key[i]) * i) % (self.size)
        return hashed_key
    
    def set(self, key, value):
        address = self._hashing_funtion(key)
        
        if self.hashmap[address] is None:
            self.hashmap[address] = [[key, value]]
        else:
            for slot in self.hashmap[address]:
                if slot[0] == key:
                    slot[1] = value
                    return None
            self.hashmap[address].append([key, value])
    
    def get(self, key):
        address = self._hashing_funtion(key)

        if self.hashmap[address] is not None:
            for slot in self.hashmap[address]:
                if slot[0] == key:
                    return slot[1]
        raise KeyError("Key Does Not Exist!")
    
    def delete(self, key):
        address = self._hashing_funtion(key)

        if self.hashmap[address] is not None:
            for slot in self.hashmap[address]:
                if slot[0] == key:
                    self.hashmap[address].remove(slot)
                    if len(self.hashmap[address]) == 0:
                        self.hashmap[address] = None
                        return None

        raise KeyError("Key Does Not Exist!")
    
    def keys(self):
        keys = []
        
        for i in self.hashmap:
            if i is not None:
                for slot in i:
                    keys.append(slot[0])
        return keys


H = HashTable(64)
