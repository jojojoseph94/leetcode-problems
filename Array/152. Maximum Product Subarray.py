"""
Logic : keep big,small and max
        At each pint update big,small and max while iterating over the array
Time Complexity : O(N)
Space : O(1)
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        big = small = nums[0]
        maximum = nums[0]
        for i in range(1, len(nums)):
            big,small = max(nums[i], nums[i]*big, nums[i]*small), min(nums[i], nums[i]*big, nums[i]*small)
            maximum = max(maximum, big)
        return maximum