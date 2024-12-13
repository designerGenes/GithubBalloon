'''
Challenge: Invert a Binary Tree

Write a Python function that takes the root node of a binary tree as input and returns the root node of the inverted tree. 
In an inverted binary tree, each node's left child becomes its right child, and vice versa. You should invert the binary tree 
in place, without creating a new tree.
'''

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root):
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

# Example usage:
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)
# inverted_root = invert_tree(root)