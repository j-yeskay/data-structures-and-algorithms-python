class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


	def __str__(self):
		return str(self.value)


def depthFirstSearchValues_recursive(root):
	if root == None:
		return []

	left_values = depthFirstSearchValues_recursive(root.left)
	right_values = depthFirstSearchValues_recursive(root.right)

	return [root.value] + left_values + right_values


def depthFirstSearchValues_iterative(root):
	stack = [ root ]
	values = []

	while stack != []:
		current = stack.pop()
		values.append(current.value)

		if current.right:
			stack.append(current.right)
		if current.left:
			stack.append(current.left)

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

print(depthFirstSearchValues_iterative(a))
print(depthFirstSearchValues_recursive(a))
	