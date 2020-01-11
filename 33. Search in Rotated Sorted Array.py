"""
Same as binary search except check if the target is in sorted part; Change lo or hi based 
on if the target is in the sorted part or not

Time complexity - O(log(N))
Space complexity - O(1)

NOTE -> If hi cannot be found (infinite length array), in a sorted array (no rotation), then 
start with lo and hi as 0, and 1. Then keep on lo = hi and hi = 2*hi
till nums[lo] <= target<=nums[hi]
NOTE 2 -> To avaoid integer overflow, 
mi = lo + (hi-lo)/2
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
            return -1
        lo = 0
        hi = len(nums) -1
        while lo <= hi:
            mi = (lo + hi)/2
            if nums[mi] == target:
                return mi
            elif nums[lo] <= nums[mi]:
                if nums[lo] <= target <=nums[mi]:
                    hi = mi-1
                else:
                    lo = mi+1
            else:
                if nums[mi] <= target <=nums[hi]:
                    lo = mi+1
                else:
                    hi = mi-1
        return -1

"""
Recursive solution
Change the loop to a recursive function call
Time complexity - O(log(N))
Space complexity - O(Nlog(N)) ??
At each function call the array is passed on.
"""

class Solution(object):
    def recursive_search(self,nums,lo,hi,target):
        if lo > hi:
            return -1
        mi = (lo+hi)/2
        if nums[mi] == target:
            return mi
        elif nums[lo] <= nums[mi]:
            if nums[lo] <= target <= nums[mi]:
                hi = mi -1
            else:
                lo = mi+1
        else:
            if nums[mi] <= target <= nums[hi]:
                lo = mi+1
            else:
                hi = mi -1
        return self.recursive_search(nums, lo, hi, target)
        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
            return -1
        return self.recursive_search(nums,0,len(nums)-1, target)