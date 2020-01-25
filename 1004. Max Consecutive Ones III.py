"""
Logic: 2 pointers start = 0 and end
       while zero_count is less than K ans = max(ans,end-start+1)
       once zero_count becomes greater than K, then keep moving start to the position 
       after first zero in previous window, then increment zero_count

Time complexity : O(N) -> You iterate over each element once
"""

class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        ans = 0
        start = 0
        zero_count = 0
        for i in range(0,len(A)):
            if A[i]==0:
                zero_count+=1
            while zero_count >K:
                if A[start]==0:
                    zero_count-=1
                start+=1
            ans = max(ans, i-start+1)
        return ans