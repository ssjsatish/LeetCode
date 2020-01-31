class TreeNode:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.data = val
root = TreeNode(1)
root.right = TreeNode(3)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.left.left = TreeNode(4)
q = []
q.append(root)
ans = []
while len(q):
	node = q[0]
	if node.left:
		q.append(node.left)
	if node.right:
		q.append(node.right)
	
	
print(root)