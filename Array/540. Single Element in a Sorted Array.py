"""
Single element in sorted array : Find position of single element through indexes.
Find mid lement, and if mid index is even and mid element is equal to its next (forward element),
then that means start to mid element does not contain the single element. So perform binary search on 
the other side..
Similarly if mid index is odd and mid element is equal to previous element, then that means
start to mid index doesnot contain the single element. Perform binary search on the other side.

Time Complexity : O(log(N))
Space complexity: O(1)
"""

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) -1
        while start<=end:
            mid = (start+end)/2
            #print "Mid, ",start, mid, end
            if mid%2==0:
                if nums[mid]==nums[mid-1]:
                    end = mid-1
                else:
                    start = mid+1
            else:
                if nums[mid]==nums[mid-1]:
                    start = mid+1
                else:
                    end = mid-1
        
        return nums[start-1]