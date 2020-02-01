"""
Logic : Do BFS keeping the sum at each level
        If node is leaf node and sum is equal to target, return target
        If none of the processed nodes are in target, return False

Time Complexity : O(N) -> We visit each node once
Space complexity : O(N) - for doing BFS we use queue
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum_):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        queue = [[root, 0]]
        while queue:
            root, val = queue.pop(0)
            if root:
                val += root.val
                if root.left == None and root.right == None:
                    if sum_ == val:
                        return True
                else:
                    queue.append([root.left, val])
                    queue.append([root.right, val])
        return False
                
        