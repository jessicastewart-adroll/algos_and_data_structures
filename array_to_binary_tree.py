'''Convert a sorted array into a binary tree, and then parallelize the algorithm.'''
class Node(object):
    def __init__(self, key):
        self.left = left
        self.right = right
        self.data = key
        
    def __repr__(self):
        return 'Node {}'.format(self.data)
        
class BinaryTree(object):
    def __init__(self, root):
        self.root = root
        
    def add_node(self, node):
        found = False
        
        current_node = self.root
        
        while not found:
            if not current_node:
                current_node = node
                found = True
            elif node.data > current_node.data:
                current_node = current_node.right
            elif node.data < current_node.data:
                current_node.left
        
    def output(self):
        leaf = self.root
        
        while leaf:
            print(leaf)
            leaf = leaf.next_node 
        

def array_to_binary_tree(sorted_array):
    '''
    input = [0, 1, 2, 3, 4]
    output = 
    '''
    midpoint = len(sorted_array)/2 if len(sorted_array) % 2 == 0 else len(sorted_array)/2 + 1
    length = len(sorted_array) - 1
    
    i = midpoint
    
    root = Node(sorted_array[midpoint])
    binary_tree = BinaryTree(root)
    
    i += 1
    
    while i <= length:
        binary_tree.add_node(sorted_array[i])
        i += 1
        
    j = midpoint - 1    
      
    while j >= 0:
        binary_tree.add_node(sorted_array[j])
        j -= 1
        
    return binary_tree   

binary_tree = array_to_binary_tree([0, 1, 2, 3, 4])
binary_tree.output()
