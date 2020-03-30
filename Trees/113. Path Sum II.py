"""
Logic : BFS, keep sum and path for each node and when reaching leaf node, check if sum == target
        If yes add to ans

Time Complexity : O(N) -> We are visiting each node exactly once
Space complexity : O(N^2) -> For each node we are keeping path to it.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum_):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        ans = []
        queue = [[root, 0, []]]
        while queue:
            root, val, path = queue.pop(0)
            if root:
                val += root.val
                path = path+[root.val]
                if root.left == None and root.right == None:
                    if sum_ == val:
                        ans.append(path)
                else:
                    queue.append([root.left, val, path])
                    queue.append([root.right, val, path])
        return ans
                