class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None


class Stack:
    def __init__(self, size):
        self.top = None
        self.bottom = None
        self.length = 0
        self.size = size
    
    def peek(self):
        return self.top
    
    def push(self, value):
        if(self.length < self.size):
            newnode = Node(value)
            if(self.length != 0):
                newnode.next = self.top
                self.top = newnode
            else:
                self.top = newnode
                self.bottom = newnode
            self.length = self.length + 1
        else:
            print("Stack OverFlow!")
    
    def pop(self):
        if(self.length != 0):
            topnode = self.top
            if(self.length == 1):
                self.top = None
                self.bottom = None
            else:
                self.top = self.top.next
            self.length = self.length - 1
            return topnode
        else:
            print("Stack UnderFlow!")

    def isempty(self):
        if(self.top == None):
            return True
        else:
            return False
    
    def display(self):
        currentnode = self.top
        while(currentnode != None):
            print(currentnode.value)
            currentnode = currentnode.next


stack = Stack(3)
