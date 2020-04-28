"""
Solution : Keep final ans array filled with nulls
           For every entry in index processed, check if the final ans array entry corresponding to it is null.
           If null, just place the nums value in the index specified.
           If not, then starting from the back of the answer array, shift one position to right
           until you reach the index specified.
           Then place the nums value
Time complexity : 2 loops O(N^2)
Space complexity : O(N)
"""

class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        final_ans = [None]*len(nums)
        for i in xrange(0,len(nums)):
            #print final_index, index[i]
            if final_ans[index[i]] == None:
                final_ans[index[i]] = nums[i]
            else:
                for j in range(len(nums)-2, index[i]-1, -1):
                    if (final_ans[j]!=None):
                        final_ans[j+1] = final_ans[j]
                final_ans[index[i]] = nums[i]
        return final_ans