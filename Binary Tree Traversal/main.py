class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



# Pre-order traversal
def pre_order(node: Node) -> list:
    if node is None:
        return []
    return [node.data] + pre_order(node.left) + pre_order(node.right)

# In-order traversal
def in_order(node: Node) -> list:
    return in_order(node.left) + [node.data] + in_order(node.right)

# Post-order traversal
def post_order(node: Node) -> list:
    return []

