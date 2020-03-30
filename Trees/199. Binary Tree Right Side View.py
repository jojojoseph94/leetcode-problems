"""
Right side view : Do BFS traversal with level as well.
At each level, the last processed non null element will be in the right view.

Time Complexity : O(N)
Space complexity : O(N) for queue

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # bfs
        ans = []
        prev_level = -1
        prev_right = None
        queue = [[root, 0]]
        while queue:
            root, level = queue.pop(0)
            if level > prev_level:
                prev_level = level
                if prev_right:
                    ans.append(prev_right.val)
                prev_right = root
            else:
                if root:
                    prev_right = root
            if root:
                queue.append([root.left,level+1])
                queue.append([root.right,level+1])           
        return ans

"""
DFS solution : Keep track of level before adding to stack. 
            At each node processed, check if it is the first element processed in that level --
            ** This is done by checking the level and the length of answers.
            If it is equal then add to result.
            Add children to the stack also.

Time complexity : O(N)
Space complexity : O(N) -> for stack
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # dfs
        ans = []
        stack = [[root, 0]]
        while stack:
            root, level = stack.pop(-1)
            if level == len(ans):
                if root:
                    ans.append(root.val)
            if root:
                stack.append([root.left,level+1])
                stack.append([root.right,level+1])           
        return ans