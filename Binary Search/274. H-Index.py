"""
H Index : Sort the numbers. Then do binary search till you find num = len(nums) - index(num)
Time complexity : O(Nlog(N)+ log(N))
Space complexity : O(1)
"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        left = 0
        right = len(citations)-1
        n = len(citations)
        citations= sorted(citations)
        while left<=right:
            mid = (left+right)/2
            if n-mid == citations[mid]:
                return n-mid
            if citations[mid]< n-mid:
                left=mid+1
            else:
                right = mid-1
        return n-left
        