class Node:
    def __new__(cls, value):
        return {
            'value' : value,
            'next' : None
        }


class LinkedList:
    def __init__(self, value):
        self.head = {
            'value' : value,
            'next' : None
        }
        self.tail = self.head
        self.length = 1
    
    def append(self, value):
        newnode = Node(value)
        self.tail['next'] = newnode
        self.tail = newnode
        self.length = self.length + 1
    
    def prepend(self, value):
        newnode = Node(value)
        newnode['next'] = self.head
        self.head = newnode
        self.length = self.length + 1

    def printlinkedlist(self):
        array = []
        currentnode = self.head
        while(currentnode != None):
            array.append(currentnode['value'])
            currentnode = currentnode['next']
        
        print(array)
    
    def insert(self, index, value):

        if index == 0:
            self.prepend(value)
        elif index >= self.length:
            self.append(value)
        else:
            currentnode = self.head
            previousnode = self.head
            counter = 0
            while(currentnode != None):
                if index == counter:
                    newnode = Node(value)
                    newnode['next'] = currentnode
                    previousnode['next'] = newnode
                    self.length = self.length + 1
                    break
                previousnode = currentnode
                currentnode = currentnode['next']
                counter = counter + 1
    
    def remove(self, index):
        if index == 0:
            self.head = self.head['next']
        else:
            currentnode = self.head
            previousnode = self.head
            counter = 0
            while(currentnode != None):
                if index == counter:
                    previousnode['next'] = currentnode['next']
                    self.length = self.length - 1
                previousnode = currentnode
                currentnode = currentnode['next']
                counter = counter + 1
                
    
    def __repr__(self):
       return f"HEAD : {self.head} \nTAIL : {self.tail} \nLENGTH : {self.length}"


l = LinkedList(20)
