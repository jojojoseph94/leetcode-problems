"""
With division, bruteforce soln
time complexity: O(N)
space: O(N)
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        prod = 1
        non_zero_prod = 1
        zero_flag = False
        for i in range(0,len(nums)):
            if nums[i]!=0:
                non_zero_prod*=nums[i]
            elif zero_flag:
                non_zero_prod = 0
            else:
                zero_flag = True
            prod*=nums[i]
        for i in range(0,len(nums)):
            if nums[i] != 0:
                ans.append(prod/nums[i])
            else:
                ans.append(non_zero_prod)
        return ans