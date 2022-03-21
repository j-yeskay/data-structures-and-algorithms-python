class Node:
    def __init__(self, value):
        self.value = value
        self.lchild = None
        self.rchild = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, parent,  value):
        if(self.root == None):
            self.root = Node(value)
        else:
            if(value < parent.value):
                if(parent.lchild == None):
                    parent.lchild = Node(value)
                else:
                    self.insert(parent.lchild, value)
            elif(value > parent.value):
                if(parent.rchild == None):
                    parent.rchild = Node(value)
                else:
                    self.insert(parent.rchild, value)
    
    def preorder(self, node):
        if(node != None):
            print(node.value)
            self.preorder(node.lchild)
            self.preorder(node.rchild)
    
    def inorder(self, node):
        if(node != None):
            self.inorder(node.lchild)
            print(node.value)
            self.inorder(node.rchild)
    
    def postorder(self, node):
        if(node != None):
            self.postorder(node.lchild)
            self.postorder(node.rchild)
            print(node.value)
    
    def is_present(self, value):
        currentnode = self.root
        while(currentnode != None):
            if(value < currentnode.value):
                currentnode = currentnode.lchild
            elif(value > currentnode.value):
                currentnode = currentnode.rchild
            elif(value == currentnode.value):
                return True
        else:
            return False
    

bst = BinarySearchTree()
bst.insert(bst.root, 100)




            




