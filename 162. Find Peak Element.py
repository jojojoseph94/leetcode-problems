"""
To find any one of the peak element, question is assuming that nums[-1] = nums[len(nums)] = -infinity
Bruteforce method is linear search. 
More efficient soln is to use binary search.
In binary search, check if mid is peak -> if yes return mid
else check which side has beginning of peak -- nums[mid] < nums[mid+1] and navigate to that side
(since nums[-1] = nums[len(nums)] = -infinity), there will be a peak at beginning or end
Time complexity : O(log(N))
Space complexity : O(1)
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums)-1
        while lo<hi:
            mi = (lo+hi)/2
            if nums[mi-1] < nums[mi] and nums[mi] > nums[mi+1]:
                return mi
            if nums[mi] <nums[mi+1]:
                lo = mi+1
            else:
                hi = mi
        return lo
        