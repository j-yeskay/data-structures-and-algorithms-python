class MyArray():
    def __init__(self):
        self.length = 0
        self.data = {}
    
    def display(self):
        print({'length' : self.length, 'data' : self.data})

    def get(self, index):
        return self.data[index]
    
    def push(self, item):
        self.data[self.length] = item
        self.length = self.length + 1
        
    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length = self.length - 1
        return last_item
    
    def delete(self, index):
        # index shifting
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        
        del self.data[self.length - 1]
        self.length = self.length - 1
    
    def update(self, index, value):
        self.data[index] = value
        

arr = MyArray()