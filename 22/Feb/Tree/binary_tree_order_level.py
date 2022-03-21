"""
#Question:
Return the level order traversal of a binary tree

struct TreeNode {
int val;
TreeNode *left;
TreeNode *right;
TreeNode() : val(0), left(nullptr), right(nullptr) {}
TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

left - small
right - big
 what is the mem and space complexity
 tree skewed
 optimise
"""
from collections import defaultdict

class binary_tree():
	"""Binary Tree"""
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
				self.righ = binary_tree(data)
			else:
				self.right.insert(data)

	def level_order_traversal(self, root, degree, state):
		#how to reduce degree before return
		degree += 1
		if root:
			state[degree].append(root.data)
			self.level_order_traversal(root.left, degree, state)
			self.level_order_traversal(root.right, degree, state)
		degree -= 1
		return state


d = defaultdict(list)
root = binary_tree(3)
root.right = binary_tree(20)
root.left = binary_tree(9)
root.right.left = binary_tree(15)
root.right.right = binary_tree(7)
#root.insert(9)
#root.insert(20)
#root.insert(15)
#root.insert(7)
print(root.left.data, root.right.data)
print(root.level_order_traversal(root, -1, d))
x = []
for i in d.keys():
	x += d[i]

print(x)



