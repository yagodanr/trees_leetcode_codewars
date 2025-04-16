# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def find_detach_right_leaf(self, root: TreeNode|None) -> TreeNode|None:
        if root is None:
            return None
        if root.right is None:
            return root
        if root.right.right is None:
            leaf = root.right
            root.right = leaf.left
            return leaf
        return self.find_detach_right_leaf(root.right)

    def deleteNode(self, root: TreeNode|None, key: int) -> TreeNode|None:
        if root is None:
            return None

        if root.val == key:
            new_root = self.find_detach_right_leaf(root.left)
            if new_root is None:
                return root.right

            if new_root.val != root.left.val:
                new_root.left = root.left

            new_root.right = root.right
            return new_root

        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        return root