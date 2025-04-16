class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n



def tree_by_levels(node: Node) -> list:
    return