# Class provided
class Node:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.children = []

def get_children_nodes(node):
    return node.children

japan = Node(1, "japan")
osaka = Node(2, "osaka")
tokyo = Node(3, "tokyo")
ginza = Node(4, "ginza")
shibuya = Node(5, "shibuya")

tokyo.children = [ginza, shibuya]
japan.children = [osaka, tokyo]

'''
# Function is provided
# return list of 0 to N Node(s) objects
get_children_nodes(node)

#Example
                 (1,"Japan")
        (2,"Osaka")           (3,"Tokyo")
(4,"Ginza")   (5,"Shibuya")

get_children_nodes(japan) -> [Node(2,"osaka"),Node(3,"tokyo")]
get_children_nodes(tokyo) -> []

# Desired Output for "build_tree"
tree = {
    'id': ObjectId,
    'data': string,
    'children': [
        {
            'id': ObjectId,
            'data': string,
            'children': [
                            {
                    'id': ObjectId,
                    'data': string,
                    'children': []
                }
            ]
        },
        {
            'id': ObjectId,
            'data': string,
            'children': []
        }
    ]
}
'''

# initial input is root node
def build_tree(node):
    tree = {}
    children = get_children_nodes(node)

    if not children:
        tree['id'] = node.id
        tree['data'] = node.data
        tree['children'] = []
        return tree

    else:
        siblings = []
        for child in children:
            siblings.append(build_tree(child))

        tree['id'] = node.id
        tree['data'] = node.data
        tree['children'] = siblings

        return tree

print(build_tree(japan))
