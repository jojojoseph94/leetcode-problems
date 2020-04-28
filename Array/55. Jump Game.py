"""
Soln: Start from second last index, with required number of jumps set as 1.
      If nums at this index is greater than req numbre of jumps, set flag to True 
      and req as 1
      Else increment req and set flag to False
           What does this mean? It means we want to check if it is possible to jump 
           2 or more indexes from a nums[i-1] 
Time complexity : O(N)
Space complexity : O(1)

NOTE: Looks like this an optimized version of DP / backtracking(??). 
TODO: Lookup DP/backtracking solutions
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #from back
        req = 1
        flag = True
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < req:
                req+=1
                flag = False
            else:
                req=1
                flag = True
        return flag
        
        