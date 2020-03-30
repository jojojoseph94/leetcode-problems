"""
Perform binary search 
1. Find the first occurance -> 
    First occurance => check if the target is same one index before, if it is then perform 
    binary search of the left part until there is no more left side to search for
2. Find last occurance
    Last occurance => check if target is same as one index after, if it is then perform 
    binary search on the right part until there is no more right side to search for
Time complexity-> O(log(N))
                to fird first occurance - O(log(N))
                to find last occurance - O(log(N))
                Total - O(log(N))
Space complexity-> O(1) - no extra space used
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == []:
            return [-1,-1]
        lo = 0
        hi = len(nums)-1
        first_occ = -1
        while lo <=hi:
            mi = (lo+hi)/2
            if nums[mi] == target:
                #check left again
                try:
                    # in python negative indexes work so that can cause issues
                    if nums[mi] == nums[mi-1] and (mi-1) >= 0:
                        hi = mi -1
                    else:
                        first_occ = mi
                        break
                except IndexError:
                    first_occ = mi
                    break
            else:
                if nums[mi] < target:
                    lo = mi+1
                else:
                    hi = mi -1
        last_occ = -1
        lo = 0
        hi = len(nums)-1
        while lo <=hi:
            mi = (lo+hi)/2
            if nums[mi] == target:
                #check right again
                try:
                    if nums[mi] == nums[mi+1]:
                        lo = mi+1
                    else:
                        last_occ = mi
                        break
                except IndexError:
                    last_occ = mi
                    break
            else:
                if nums[mi] < target:
                    lo = mi+1
                else:
                    hi = mi -1
        return [first_occ, last_occ]
        