"""
Logic : Do inorder traversal and store the nodes in an array
        Then sort the array using sorting algorithm just by swapping the values only

Time complexity : O(N^2) -> Sorting using bubble sort
Space complexity : O(N) -> To store the full tree in an array, and recursion stack
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        nodes = []
        #inorder traversal
        def inorder(node):
            if node:
                inorder(node.left)
                nodes.append(node)
                inorder(node.right)
        def swap(node1, node2):
            temp = node1.val
            node1.val = node2.val
            node2.val = temp
        inorder(root)
        #bubble sort
        for i in range(0,len(nodes)):
            for j in range(0,len(nodes)-i-1):
                if nodes[j].val > nodes[j+1].val:
                    #swap
                    swap(nodes[j], nodes[j+1])

"""
Logic Inorder traversal with 2 nodes only instead of storing full nodelist

Time complexity : O(N)
Space complexity : O(N)-> recursion stack
"""

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.swap1 = None
        self.swap2 = None
        #inorder traversal
        def inorder(node):
            if node:
                inorder(node.left)
                if self.prev == None:
                    self.prev = node
                if self.swap1 == None:
                    if node.val < self.prev.val:
                        self.swap1 = self.prev
                if self.swap1!=None:
                    if node.val < self.prev.val:
                        self.swap2 = node
                self.prev = node
                inorder(node.right)
        def swap(node1, node2):
            temp = node1.val
            node1.val = node2.val
            node2.val = temp
        inorder(root)
        swap(self.swap1,self.swap2)

"""
TODO: O(1) space complexity solution 
Morris inorder traversal 
"""
