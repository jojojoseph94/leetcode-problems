"""
Algo : Dynamic programming
       At each point maximize (nums[i] + solution at 2 steps back, solution at one step back)
Time complexity : O(N)
Space complexity : O(N)
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # start with first house
        dp = [None]*(len(nums)+1)
        dp[0] = 0
        if nums == []:
            return 0
        dp[1] = nums[0]
        for i in range(1,len(nums)):
            dp[i+1] = max(nums[i] + dp[i-1], dp[i])
        #print dp[-1]
        return dp[-1]