# Class provided
class Node:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.children = []

def get_children_nodes(node):
    return node.children

animals = Node(1, "Animals")
dogs = Node(2, "Dogs")
cats = Node(3, "Cats")
beagles = Node(4, "Beagles")
bulldogs = Node(5, "Bulldogs")

dogs.children = [beagles, bulldogs]
animals.children = [dogs, cats]

'''
# Function is provided
# return list of 0 to N Node(s) objects
get_children_nodes(<ObjectId>)

#Example
                 (1,"Animals")
        (2,"Dog")           (3,"Cat")
(4,"Beagle")   (5,"Bulldog")

get_children_nodes(1) -> [Node(2,"Dog"),Node(3,"Cat")]
get_children_nodes(3) -> []

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

print(build_tree(animals))
