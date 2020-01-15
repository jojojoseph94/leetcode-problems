"""
Bruteforce soln : For every element in array, starting with index to length
                  if element is zero, decrease count
                  if element is one, increase count
                  if count = 0, check if greater than max length
Time complexity : O(N^2)
Leetcode Time Exceeded
"""
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(0,len(nums)):
            this_c = 0
            for j in range(i,len(nums)):
                if nums[j] == 0:
                    this_c-=1
                else:
                    this_c+=1
                if this_c == 0:
                    ans = max(ans,j-i+1)
        return ans

"""
Solution2 : 
"""
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        this_c = 0
        hash_ = {0:-1}
        for i in range(0,len(nums)):
            if nums[i] == 0:
                this_c -=1
            else:
                this_c+=1
            if this_c in hash_:
                ans = max(ans,i - hash_[this_c])
            else:
                hash_[this_c] = i
        return ans