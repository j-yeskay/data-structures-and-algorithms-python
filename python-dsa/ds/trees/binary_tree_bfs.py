class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


	def __str__(self):
		return str(self.value)


def breadthFirstSearchValues_iterative(root):
	queue = [ root ]
	values = []

	while queue != []:
		current = queue.pop(0)
		values.append(current.value)

		if current.left:
			queue.append(current.left)

		if current.right:
			queue.append(current.right)


	return values


def level_order_traversal(root):
	if root == None:
		return None
	else:
		values = []
		queue = [root]

		while queue != []:
			length = len(queue)
			values.append([])
			for i in range(length):
				currentnode = queue.pop(0)
				values[-1].append(currentnode.value)
				if currentnode.left:
					queue.append(currentnode.left)
				if currentnode.right:
					queue.append(currentnode.right)
		return values


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

# 		a
# 	   / \
# 	  b   c
# 	 / \   \
# 	d   e   f

print(breadthFirstSearchValues_iterative(a))
