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

"""
Without division : Keep 2 arrays, one for left products and one for right products.
                   Answer is the product of these 2
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0]*len(nums)
        left = [0]*len(nums)
        right = [0]*len(nums)
        left[0] = 1
        right[-1] = 1
        for i in range(1,len(nums)):
            left[i] = left[i-1]*nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1]*nums[i+1]
        for i in range(0,len(nums)):
            ans[i] = left[i]*right[i]
        return ans