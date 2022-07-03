class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


def tree_sum_recursive(root):
    if root == None:
        return 0

    left_sum = tree_sum_recursive(root.left)
    right_sum = tree_sum_recursive(root.right)

    return root.value + left_sum + right_sum


def tree_sum_iterative(root):
    stack = [ root ]
    tree_sum = 0

    while stack != []:
        current = stack.pop()
        tree_sum = tree_sum + current.value

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return tree_sum


one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)

one.left = two
one.right = three

two.left = four
two.right = five

three.right = six

print(tree_sum_recursive(one))
print(tree_sum_iterative(one))
