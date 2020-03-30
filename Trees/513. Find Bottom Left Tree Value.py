"""
Logic: Do BFS while storing the first element in each level
Time complexity : O(N)
Space complexity : O(2^log(N))
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #bfs
        queue = [root]
        while queue:
            i = len(queue)
            j = 0
            this_level = False
            while j<i:
                node = queue.pop(0)
                if node:
                    if this_level == False:
                        last_ele = node.val
                        this_level = True
                    queue.append(node.left)
                    queue.append(node.right)
                j+=1
        return last_ele
        