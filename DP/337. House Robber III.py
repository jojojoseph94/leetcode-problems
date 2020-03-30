"""
Bruteforce solution : at each level maximize robbing that node and 4 grandchildren nodes
                      or skipping that node and robbing its children

Time Complexity : Exponential

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #bruteforce
        if root == None:
            return 0
        val1=root.val
        if root.left!=None:
            val1+= self.rob(root.left.left) + self.rob(root.left.right)
        if root.right!=None:
            val1+= self.rob(root.right.left) + self.rob(root.right.right)
        return max(val1, self.rob(root.left) + self.rob(root.right))

"""
Naive DP solution : Use a hashmap to store the result found at each node
                    This way the repeating subproblems can be eliminated
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self,root):
        return self.robSub(root, {})
    
    def robSub(self, root, hashmap):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root in hashmap:
            return hashmap[root]
        #bruteforce
        if root == None:
            return 0
        val1=root.val
        if root.left!=None:
            val1+= self.robSub(root.left.left, hashmap) + self.robSub(root.left.right, hashmap)
        if root.right!=None:
            val1+= self.robSub(root.right.left, hashmap) + self.robSub(root.right.right, hashmap)
        hashmap[root] = max(val1, self.robSub(root.left, hashmap) + self.robSub(root.right, hashmap))
        return hashmap[root]
        
"""
Greedy solution : At each level return both robbed and not robbed options
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self,root):
        return max(self.robSub(root))
    
    def robSub(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return [0,0]
        left = self.robSub(root.left)
        right = self.robSub(root.right)
        res = [0,0]
        res[0] = max(left[0],left[1]) + max(right[0],right[1]) 
        res[1] = root.val + left[0] + right[0]
        print res
        return res