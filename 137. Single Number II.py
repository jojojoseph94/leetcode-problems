"""
Single number - II
                logic - Use hashmap for each element. If count becomes 3 remove it.

                The key of the final remaining element in the hashmap will be the answer
Time Complexity : O(N)
Space complexity : O(N)
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_ = {}
        for i in nums:
            if i in dict_:
                if dict_[i] == 1:
                    dict_[i]+=1
                else:
                    del dict_[i]
            else:
                dict_[i] = 1
        return dict_.keys()[0]
        