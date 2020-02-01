"""
Cousins in binary tree -> BFS soln. 
                          Find x_parent and y_parent
                          then x_level and y_level
                          then if x_parent!=y_parent and x_level == y_level
                            return True
                          else
                            return False

Time complexity : O(N) -> May need to visit all the nodes

Space complexity : O(N) -> for queue


"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        x_depth = 0
        y_depth = 0
        x_parent = None
        y_parent = None
        found = 0
        if x == root.val or y == root.val:
            return False
        queue = [[root,0]]
        while queue:
            root,level = queue.pop(0)
            if root:
                if (root.left!=None and root.left.val == x) or (root.right != None and root.right.val == x):
                    x_parent = root
                    x_depth = level+1
                    found+=1
                elif (root.left!=None and root.left.val == y) or (root.right != None and root.right.val == y):
                    y_parent = root
                    y_depth = level+1
                    found+=1
                if found == 2:
                    break
                queue.append([root.left, level+1])
                queue.append([root.right, level+1])
        #print x_parent, y_parent, x_depth, y_depth
        if x_parent != y_parent and x_depth == y_depth:
                 return True
        else:
                 return False
                 
                 
                
        