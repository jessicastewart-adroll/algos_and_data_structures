class TreeNode(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def __repr__(self):
		left = self.left.data if self.left else None
		right = self.right.data if self.right else None
		return 'data: {}, left: {} right: {}'.format(self.data, left, right)

def preorder(node):
	if not node:
		return
	else:
		print(node.data)
		preorder(node.left)
		preorder(node.right)

def inorder(node):
	if not node:
		return
	else:
		inorder(node.left)
		print(node.data)
		inorder(node.right)

def postorder(node):
	if not node:
		return
	else:
		postorder(node.left)
		postorder(node.right)
		print(node.data)


root = TreeNode(25)
fifteen = TreeNode(15)
ten = TreeNode(10)
four = TreeNode(4)
twelve = TreeNode(12)
twenty_two = TreeNode(22)
twenty_four = TreeNode(24)
eighteen = TreeNode(18)
fifty = TreeNode(50)
thirty_five = TreeNode(35)
thirty_one = TreeNode(31)
forty_four = TreeNode(44)
seventy = TreeNode(70)
sixty_six = TreeNode(66)
ninety = TreeNode(90)

root.left = fifteen
root.right = fifty
fifteen.left = ten
fifteen.right = twenty_two
ten.left = four
ten.right = twelve
twenty_two.left = eighteen
twenty_two.right = twenty_four
fifty.left = thirty_five
fifty.right = seventy
thirty_five.left = thirty_one
thirty_five.right = forty_four
seventy.left = sixty_six
seventy.right = ninety

# inorder(root)
# 4 10 12 15 18 22 24 25 31 35 44 50 66 70 90

# preorder(root)
# 25 15 10 4 12 22 18 24 50 35 31 44 70 66 90

# postorder(root)
# 4 12 10 18 24 22 15 31 44 35 66 90 70 50 25 
