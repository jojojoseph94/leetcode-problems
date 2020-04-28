"""
Solution : Convert to binary. Store indexes of 1's. 
           Find maximum distance between the adjacent differences
           return
Time complexity : O(N), N being the number of bytes needed to represent the number
Space complexity : O(N), depends on the number indexes stored.
"""

class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        # store indexes
        indexes = []
        c = 0
        for i in bin(N)[2:]:
            if i == "1":
                indexes.append(c)
            c+=1
        #print indexes
        if len(indexes) > 1:
            return max(indexes[i+1] - indexes[i] for i in xrange(0,len(indexes)-1))
        else:
            return 0
        