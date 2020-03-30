"""
To find min element, do binary search on all the unsorted parts.
If there is no unsorted part, return nums[low]
When searching in second subarray, include the mid also in the search

Time complexity - O(log(N))
Space complexity - O(1)
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return -1
        lo = 0
        hi = len(nums)-1
        while lo<=hi:
            mi = (lo+hi)/2
            if nums[lo] <= nums[mi] <=nums[hi]:
                return nums[lo]
            elif nums[lo] <= nums[mi]:
                lo = mi+1
            else:
                hi = mi