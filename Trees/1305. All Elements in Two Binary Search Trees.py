"""
Logic: inorder traversal on both trees while storing in separate lists
       Then merge the two lists
Time complexity : O(NlogN) -> For sorting the lists
Space complexity : O(N)
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        list1 = []
        list2 = []
        l1 = False
        def inorder(node):
            if node:
                inorder(node.left)
                if l1:
                    list2.append(node.val)
                else:
                    list1.append(node.val)
                inorder(node.right)
        inorder(root1)
        l1 = True
        inorder(root2)
        return sorted(list1+list2)
        