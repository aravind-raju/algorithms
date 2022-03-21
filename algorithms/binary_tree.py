class binary_tree():
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data
	def insert(self, data):
		if data < self.data:
			if self.left is None:
				self.left = binary_tree(data)
			else:
				self.left.insert(data)
		else:
			if self.right is None:
				self.right = binary_tree(data)
			else:
				self.right.insert(data)
	def in_order_traversal(self, root):
		res = []
		if root:
			res = self.in_order_traversal(root.left)
			res.append(root.data)
			res = res + self.in_order_traversal(root.right)
		return res
	def pre_order_traversal(self, root):
		res = []
		if root:
			res.append(root.data)
			res += self.pre_order_traversal(root.left)
			res += self.pre_order_traversal(root.right)
		return res
	def post_order_traversal(self, root):
		res = []
		if root:
			res += self.post_order_traversal(root.left)
			res += self.post_order_traversal(root.right)
			res.append(root.data)
		return res
	def top_view(self, root):
		if root:
			print(root.data)
			print(self.pre_order_traversal(root.left))
			print(self.pre_order_traversal(root.right))
	def search(self, root, key):
	    if root is None:
	    	return "Value not found" 

	    if root.data == key:
	        return root.data
	 
	    if root.data < key:
	        return self.search(root.right,key)
	   
	    return self.search(root.left,key)
 


root = binary_tree(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.in_order_traversal(root))
print(root.pre_order_traversal(root))
print(root.post_order_traversal(root))
print(root.search(root, 10))
print(root.search(root, 100))