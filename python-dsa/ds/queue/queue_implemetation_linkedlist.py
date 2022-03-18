class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def peek(self):
        return self.first
    
    def enqueue(self, value):
        newnode = Node(value)
        if(self.length == 0):
            self.first = newnode 
            self.last = newnode
        else:
            self.last.next = newnode 
            self.last = newnode 
        self.length = self.length + 1
    
    def dequeue(self):
        firstnode = self.first 
        self.first = self.first.next
        self.length = self.length - 1 
        return firstnode
    
    def isempty(self):
        if(self.length == 0):
            return True 
        else:
            return False
        
    def display(self):
        currentnode = self.first 
        while(currentnode != None):
            print(currentnode.value)
            currentnode = currentnode.next


queue = Queue()
