"""
Logic : Do BFS while generating sum at each level
        If leaf node, add to ans

Time complexity : O(N) -> Need to visit each node exactly once
Space complexity : Using queue for BFS, so O(N)

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        queue = [[root, 0]]
        while queue:
            root, val = queue.pop(0)
            if root:
                val = val*10 + root.val
                #check if leaf node, if so add to ans
                if root.left == None and root.right == None:
                    ans+= val
                else:
                    queue.append([root.left, val])
                    queue.append([root.right, val])
        return ans
        