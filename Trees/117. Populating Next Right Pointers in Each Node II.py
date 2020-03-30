"""
Logic : Same as 116 but whenever you encounter null nodes in both left and right, go to next and check for non null nodes.
        This is applicable for level travesal and horizontal traversal. 

Time complexity : O(N) -> All nodes are visited exactly once
Space complexity : O(1) -> Only four pointers are used -> 
                    prev, cur, level, new_level


"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        level = root
        cur = root.left
        while level:
            #print level.val
            prev = None
            new_level = level
            if new_level.left:
                cur = new_level.left
            elif new_level.right:
                cur = new_level.right
            else:
                #loopty loop
                new_level = new_level.next
                while new_level:
                    if new_level.left:
                        cur = new_level.left
                        break
                    elif new_level.right:
                        cur = new_level.right
                        break
                    else:
                        new_level = new_level.next
            while cur:
                #print "New level", new_level.val
                if prev:
                    prev.next = cur
                prev = cur
                if new_level:
                    if new_level.right == cur or new_level.right == None:
                        new_level = new_level.next
                        while new_level:
                            #print "At new_level lloop"
                            if new_level.left:
                                cur = new_level.left
                                break
                            elif new_level.right:
                                cur = new_level.right
                                break
                            else:
                                new_level = new_level.next
                        if cur == prev:
                            break
                    else:
                        cur = new_level.right
                else:
                    break
            if level.left:
                level = level.left
            elif level.right:
                level = level.right
            else:
                #loopty loop
                level = level.next
                while level:
                    if level.left:
                        level = level.left
                        break
                    elif level.right:
                        level = level.right
                        break
                    else:
                        level = level.next
        return root
        