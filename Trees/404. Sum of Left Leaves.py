"""
Normal BFS with a flag for left children
Time complexity : O(N)
Space complexity : (N)

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [[root, False]]
        sum_ = 0
        while queue:
            root, left = queue.pop(0)
            if root:
                if root.left == None and root.right == None:
                    # leaf node
                    if left:
                        sum_+=root.val
                queue.append([root.left, True])
                queue.append([root.right, False])
        return sum_