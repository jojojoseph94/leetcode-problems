"""
To invert a tree do breadth first traversal and then swap the left and right children
Time Complexity : O(N) -> Each node is visited once
Space complexity : O(1)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root
        