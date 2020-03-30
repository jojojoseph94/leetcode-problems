"""
Logic : If the houses are circular, then the problem can be divided into
        house 0 to n-2 and houses 1 to n-1
        Then return the max of the 2
        The divided problems can be solved using
        dp[i] = max(nums[i]+dp[i-2], dp[i-1])

Time complexity : O(N)
Space complexity : O(N)
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [None]*(len(nums)+1)
        dp[0] = 0
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        dp[1] = nums[0]
        for i in range(1,len(nums)-1):
            dp[i+1] = max(nums[i] + dp[i-1], dp[i])
        
        val1 = dp[-2]
        dp[0] = 0
        dp[1] = 0
        for i in range(1,len(nums)):
            dp[i+1] = max(nums[i] + dp[i-1], dp[i])
        #print val1, dp[-1]
        return max(val1, dp[-1])
        
        