"""
Logic : Do BFS traversal. At each level start with previous set as None
        Then if previous, set node.next as previous
        Set node as previous and continue with BFS

TimeComplexity : BFS traversal; O(N)
Space complexity : O(2^log(N)) -> O(2 to the power h where h is hte height of the tree)
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        #bfs
        original_root = root
        queue = [root]
        
        while queue:
            i = len(queue)
            prev = None
            while i:
                root = queue.pop(0)
                if prev!=None:
                    prev.next = root
                if root:
                    queue.append(root.left)
                    queue.append(root.right)
                    prev = root
                    i-=1
        return original_root

"""
2 pointers : Keep one pointer for going level by level and one for traversing to the right at each point

Time complexity : O(N)
Space complexity : O(1)
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        prev = root
        level = root
        if level == None:
            return None
        while level.left:
            prev = level
            while prev:
                prev.left.next = prev.right
                if prev.next:
                    prev.right.next = prev.next.left
                prev = prev.next
            level = level.left
        return root